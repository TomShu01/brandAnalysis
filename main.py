from langgraph.graph import END, StateGraph, START
from shared import GraphState
# import agents:
from researcher_agent import researcher_agent
from analysis_agent import analysis_agent
from writer_agent import writer_agent

# Define main graph
graph = StateGraph(GraphState)

# Include nodes in main graph
graph.add_node("researcher_agent", researcher_agent)
graph.add_node("analysis_agent", analysis_agent)
graph.add_node("writer_agent", writer_agent)

# Define edges in main graph
graph.add_edge(START, "researcher_agent")
graph.add_edge("researcher_agent", "analysis_agent")
graph.add_edge("analysis_agent", "writer_agent")
graph.add_edge("writer_agent", END)

graph = graph.compile()

if __name__ == "__main__":
    """
    spins up a simple CLI interface for interacting with the agent
    """
    while True:
        try:
            user_input = input("Enter brand name (type quit, exit, or q to quit): ")
            if user_input.lower() in ["quit", "exit", "q"]:
                print("Goodbye!")
                break

            result = graph.invoke({'brand': user_input})
            result["report"].pretty_print() 
        except Exception as e:
            print("error occurred during inference:")
            print(e)
            break