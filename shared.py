#!/usr/bin/python3.10
# Contains vector database definition and state definitions
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from typing_extensions import TypedDict
from typing import Annotated
from operator import add
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# import API keys from environment variables
load_dotenv()

# define LLM models
llm = ChatOpenAI(model="gpt-4o")
reasoning_llm = ChatOpenAI(model="o1-mini")

# define vector database
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

vector_store = Chroma(
    collection_name="brand_analysis",
    embedding_function=embeddings,
    persist_directory="./chroma_langchain_db",  # Where to save data locally, remove if not necessary
)

# Define states
# Base classes for state
class BrandState(TypedDict):
    brand: str

class ReportState(TypedDict):
    report: str

class BrandDocState(BrandState):
    documents: Annotated[list, add]

# internal state for agents:
class ResearcherInternalState(BrandDocState):
    query: str
    loop_count: int

class AnalysisInternalState(BrandDocState):
    derived_documents: Annotated[list, add]

class WriterInternalState(BrandState, ReportState):
    notes: str

# State for the parent agent
class GraphState(BrandDocState, ReportState):
    pass