# news-bot

LLM-powered bot to gather top ten news articles from the web

## Installation

Create and activate a virtual environment

- Using Conda:
  ```sh
  conda create --name news-bot-env python=3.10 -y
  conda activate news-bot-env
  pip install -r requirements.txt
  ```

## Configuration

Create a .env file

- In the root directory of the project, create a .env file and add your API keys:

  ```
  GROQ_API_KEY=your_groq_api_key_here
  OPEN_API_KEY=your_openrouter_api_key_here
  ```

  Note: If you're only using one provider, you can leave the other key empty.
