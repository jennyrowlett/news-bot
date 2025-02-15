import langgraph
from langchain_ollama.llms import OllamaLLM


def process_date(selected_date):
    # Perform any backend processing with the date
    return selected_date


# Function to query LLM with the selected date
def query_llm(selected_date):
    prompt = f"List 10 interesting news headlines from {selected_date.strftime('%B %d, %Y')}."
    
    # Simulating an LLM response (replace with actual API call)
    try:
        model = OllamaLLM(model="llama3.2")
        return model.invoke(prompt)
    except Exception as e:
        return f"Error querying LLM: {str(e)}"
