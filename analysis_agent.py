from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langgraph.graph import END, StateGraph, START
from langchain.schema import Document
from shared import vector_store, BrandState, BrandDocState, AnalysisInternalState, llm, reasoning_llm
from prompts import trend_query, social_signal_query, topics_query, sentiment_query

# Graph definition
analysis_agent = StateGraph(AnalysisInternalState, input=BrandDocState, output=BrandState)

def analysis(state: AnalysisInternalState, query):
    """
    Instructs the LLM model to perform analysis on the state according to query

    Args:
        state (dict): The current graph state
        query: the prompt that instructs the model to perform analysis

    Returns:
        state (dict): Updates derived_documents key with a re-phrased question
    """

    print("---CONDUCTING ANALYSIS ON SPECIFIC TOPIC---")
    prompt_template = PromptTemplate.from_template(query)
    analysis_llm = prompt_template | llm
    doc = analysis_llm.invoke({"brand": state["brand"], "documents": str(state["documents"])})
    vector_store.add_documents(documents=[Document(page_content=str(doc), metadata={"type": "derived"})])

    return {"derived_documents": [doc]}

# define nodes in the graph
def trend_analysis(state: BrandDocState):
    """
    Calls the analysis function to perform analysis on the trend_query prompt

    Args:
        state (dict): The current graph state

    Returns:
        state (dict): Updates graph state based on analysis
    """

    return(analysis(state, trend_query))

def social_signal_analysis(state: BrandDocState):
    """
    Calls the analysis function to perform analysis on the social_signal_query prompt

    Args:
        state (dict): The current graph state

    Returns:
        state (dict): Updates graph state based on analysis
    """
    
    return(analysis(state, social_signal_query))

def topics_analysis(state: BrandDocState):
    """
    Calls the analysis function to perform analysis on the topics_query prompt

    Args:
        state (dict): The current graph state

    Returns:
        state (dict): Updates graph state based on analysis
    """
    
    return(analysis(state, topics_query))

def sentiment_analysis(state: BrandDocState):
    """
    Calls the analysis function to perform analysis on the sentiment_query prompt

    Args:
        state (dict): The current graph state

    Returns:
        state (dict): Updates graph state based on analysis
    """

    return(analysis(state, sentiment_query))

def generate_recommendations(state: AnalysisInternalState):
    """
    Generates recommendations for the brand based on derived_documents from previous analysis nodes

    Args:
        state (dict): The current graph state

    Returns:
        state (dict): Updates derived_documents to add the recommendations
    """

    print("---GENERATE RECOMMENDATIONS FOR THE BRAND---")
    prompt = ChatPromptTemplate.from_messages(
        [("user",
          """
          Generate recommendations for {brand}, such as Strategic opportunities or actionables to win over new audiences.
          
          You have the following reports on the brand's current social perceptions:
          {derived_documents}
          """)],
    )
    chain = prompt | reasoning_llm
    doc = chain.invoke({"brand": state["brand"], "derived_documents": state["derived_documents"]})
    vector_store.add_documents(documents=[Document(page_content=str(doc), metadata={"type": "derived"})])
    return {"derived_documents": [doc]}

# add nodes to graph
analysis_agent.add_node("trend_analysis", trend_analysis)
analysis_agent.add_node("social_signal_analysis", social_signal_analysis)
analysis_agent.add_node("topics_analysis", topics_analysis)
analysis_agent.add_node("sentiment_analysis", sentiment_analysis)
analysis_agent.add_node("generate_recommendations", generate_recommendations)

# add edges to graph
analysis_agent.add_edge(START, "trend_analysis")
analysis_agent.add_edge(START, "social_signal_analysis")
analysis_agent.add_edge(START, "topics_analysis")
analysis_agent.add_edge(START, "sentiment_analysis")
analysis_agent.add_edge("trend_analysis", "generate_recommendations")
analysis_agent.add_edge("social_signal_analysis", "generate_recommendations")
analysis_agent.add_edge("topics_analysis", "generate_recommendations")
analysis_agent.add_edge("sentiment_analysis", "generate_recommendations")
analysis_agent.add_edge("generate_recommendations", END)

# Compile our agent
analysis_agent = analysis_agent.compile()