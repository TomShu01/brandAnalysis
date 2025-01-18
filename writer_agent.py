from langchain_core.prompts import PromptTemplate
from langgraph.graph import END, StateGraph, START
from shared import vector_store, BrandState, ReportState, WriterInternalState, llm
from prompts import report_template, generate_report_prompt
from config import sections

# Graph definition
writer_agent = StateGraph(WriterInternalState, input=BrandState, output=ReportState)

# define nodes in the graph
def gather_info_node(state: BrandState):
    """
    retrieves documents from the vector database and organizes the notes on the brand

    Args:
        state (dict): The current graph state

    Returns:
        state (dict): Updates notes key with an organized collection of info about the brand
    """

    print("---ORGANIZE RESEARCH ON BRAND---")
    notes = ""
    
    for section in sections:
        query = section["title"] + "about " + state["brand"] + ": " + section["section"]
        docs = vector_store.similarity_search(query)
        docs = ["Content:\n" + doc.page_content + "\nmetadata:\n" + str(doc.metadata) for doc in docs]
        notes+= section["title"] + ": \n" + str(docs) + "\n"
    
    # summarized_notes = llm.invoke("summarize the following such that its size is reduced by half" + notes)
    
    return({"notes": notes})

def generate_report_node(state: WriterInternalState):
    """
    Generates a report on the brand based on collected info on the brand from notes
    and a template for the report

    Args:
        state (dict): The current graph state

    Returns:
        state (dict): Updates report key with the generated report
    """

    print("---GENERATE FINAL REPORT ON BRAND---")
    report_generation_template = PromptTemplate.from_template(generate_report_prompt)
    report_generate = report_generation_template | llm
    return({"report": report_generate.invoke({"brand": state["brand"], "notes": state["notes"], "template": report_template})})

# add nodes to graph
writer_agent.add_node("gather_info_node", gather_info_node)
writer_agent.add_node("generate_report_node", generate_report_node)

# add edges to graph
writer_agent.add_edge(START, "gather_info_node")
writer_agent.add_edge("gather_info_node", "generate_report_node")
writer_agent.add_edge("generate_report_node", END)

# Compile our agent
writer_agent = writer_agent.compile()