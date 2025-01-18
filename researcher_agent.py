#!/usr/bin/python3.10
from langchain_core.prompts import PromptTemplate
from langgraph.graph import END, StateGraph, START
from langchain.schema import Document
from langchain_community.tools.tavily_search import TavilySearchResults
from shared import vector_store, InputState, OutputState, OverallState, llm
from prompts import initial_query

# import useful chains
from chains.grade_doc_chain import doc_grader
from chains.query_rewriter import query_rewriter

# import API keys from environment variables
from dotenv import load_dotenv
load_dotenv()

# Graph definition
researcher_agent = StateGraph(OverallState, input=InputState, output=OutputState)

# define nodes in the graph
def initialize_query_node(state: InputState):
    """
    Initializes the search query passed into Tavily to perform the initial web search

    Args:
        InputState(dict): The current graph state which includes the brand
    
    Returns:
        state (dict): Updates the query key in graph state
    """
    
    return {"query" : initial_query}

def web_search_node(state: OverallState):
    """
    Performs Tavily web search on the brand using query from state

    Args:
        state (dict): The current graph state
    
    Returns:
        state (dict): Updates the documents key in graph state
    """

    prompt_template = PromptTemplate.from_template(state["query"])
    formatted_query = prompt_template.format(brand=state["brand"])
    web_search_tool = TavilySearchResults(max_results=2)
    docs = web_search_tool.invoke({"query": formatted_query})

    return {"documents": docs}

def eval_edge(state: OverallState):
    """
    Determines whether the retrieved documents are relevant to the question.

    Args:
        state (dict): The current graph state

    Returns:
        str: Yes or No
    """

    print("---CHECK DOCUMENT RELEVANCE TO QUESTION---")
    brand = state["brand"]
    documents = state["documents"]

    score = doc_grader(llm).invoke(
        {"question": brand, "document": str([doc["content"] for doc in documents])}
    )
    grade = score.binary_score
    return grade

def transform_query_node(state: OverallState):
    """
    Transform the query to produce a better question.

    Args:
        state (dict): The current graph state

    Returns:
        state (dict): Updates question key with a re-phrased question
    """

    print("---TRANSFORM QUERY---")
    query = state["query"]

    # Re-write question
    better_query= query_rewriter(llm).invoke({"query": query})
    return {"query": better_query}

def insert_db_node(state: OverallState):
    """
    Inserts documents to the vector database

    Args:
        state (dict): The current graph state

    Returns:
        Empty object
    """

    documents = [
        Document(page_content=doc["content"], metadata={"url": doc["url"], "type": "fact"})
        for doc in state["documents"]
    ]

    vector_store.add_documents(documents=documents)
    
    return {}

# add nodes to graph
researcher_agent.add_node("initialize_query_node", initialize_query_node)
researcher_agent.add_node("web_search_node", web_search_node)
researcher_agent.add_node("transform_query_node", transform_query_node)
researcher_agent.add_node("insert_db_node", insert_db_node)

# add edges to graph
researcher_agent.add_edge(START, "initialize_query_node")
researcher_agent.add_edge("initialize_query_node", "web_search_node")
researcher_agent.add_conditional_edges(
    "web_search_node",
    eval_edge,
    {
        "yes": "insert_db_node",
        "no": "transform_query_node",
    },
)
researcher_agent.add_edge("insert_db_node", END)
researcher_agent.add_edge("transform_query_node", "web_search_node")

# Compile our agent
researcher_agent = researcher_agent.compile()