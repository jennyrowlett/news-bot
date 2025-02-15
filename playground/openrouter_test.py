#file to test open router
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=api_key,
)

completion = client.chat.completions.create(
  extra_body={},
  model="deepseek/deepseek-r1:free",
  messages=[
    {
      "role": "user",
      "content": "What is the meaning of life?"
    }
  ]
)
print(completion)