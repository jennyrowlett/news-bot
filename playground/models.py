import os
import click
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables
load_dotenv()

def get_api_key(provider):
    """Retrieve the API key based on the provider."""
    env_var = "GROQ_API_KEY" if provider == "groq" else "OPENAI_API_KEY"
    api_key = os.getenv(env_var)

    if not api_key:
        raise ValueError(f"Error: API key for {provider} is missing. Check your .env file.")

    return api_key

def initialize_model(provider, model):
    """Initialize the language model based on the provider."""
    if provider == "groq":
        return ChatGroq(model=model)
    elif provider == "openrouter":
        return ChatOpenAI(model=model, base_url="https://openrouter.ai/api/v1")

@click.command()
@click.option(
    '--provider', '-p', 
    type=click.Choice(["groq", "openrouter"], case_sensitive=False), 
    default="groq", 
    show_default=True, 
    help="Model provider (groq or openrouter)"
)
@click.option('--model', '-m', default="llama3-70b-8192", show_default=True, help="Model name")

def main(provider, model):
    """CLI that accepts a provider name and model name."""
    provider = provider.lower()  # Make provider case-insensitive
    click.echo(f'Using provider: {provider}, model: {model}')

    try:
        api_key = get_api_key(provider)
        llm = initialize_model(provider, model)

        # Define the prompt template
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a helpful assistant that translates {input_language} to {output_language}."),
            ("human", "{input}"),
        ])

        # Create the chain
        chain = prompt | llm

        # Execute the chain
        response = chain.invoke({
            "input_language": "English",
            "output_language": "German",
            "input": "I love programming.",
        })

        # Display the result
        print(response)

    except ValueError as e:
        click.echo(str(e), err=True)

if __name__ == '__main__':
    main()
