from langchain_ollama.llms import OllamaLLM
from langchain_core.messages import HumanMessage, SystemMessage
import langgraph
from langgraph.prebuilt import ToolNode
from langchain_core.tools import tool
from langchain_core.output_parsers import JsonOutputKeyToolsParser
from pydantic import BaseModel
from typing import List
import requests
from langgraph.graph import StateGraph, START, END
from IPython.display import Image, display
from typing_extensions import TypedDict



# def process_date(selected_date):
#     # Perform any backend processing with the date
#     return selected_date


# Function to query LLM with the selected date
def query_llm(selected_date):
        
    # Simulating an LLM response (replace with actual API call)
    try:
        model = OllamaLLM(model="llama3.2")
    except Exception as e:
        raise f"Error querying LLM: {str(e)}"

    # Google Search API setup
    API_KEY = ""
    CX = "news-bot"
    SEARCH_URL = "https://cse.google.com/cse?cx=12008bbfed3b34555"

    # Define output structure
    class Article(TypedDict):
        title: str
        url: str

    def search_web(State) -> List[Article]:
        """Search the web using Google Custom Search API and return the 10 most recent articles."""
        params = {
            "q": query,
            "key": API_KEY,
            "cx": CX,
            "num": 10
        }
        response = requests.get(SEARCH_URL, params=params)
        results = response.json().get("items", [])
        for item in results:
            Article["title"]=item["title"] 
        return {"title": results}
    # Register tool
    search_tool = ToolNode([search_web])  # Wrap function in a list

    # Define the LangGraph workflow
    graph = StateGraph(Article)
    graph.add_node("search", search_tool)
    graph.add_edge(START, "search")
    graph.add_edge("search", END)

    graph = graph.compile()
    
    # Run the agent
    query = f"latest news from {selected_date}"
    result = graph.invoke({"query": query})

    # Output results
    for idx, article in enumerate(result, 1):
        print(f"{idx}. {article.title} - {article.url}")

query_llm("October 2 2003")