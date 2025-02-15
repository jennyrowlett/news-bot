#File to test groq
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
api_key = os.getenv('GROQ_API_KEY')

client = Groq(
    api_key=api_key,
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "WAP to generate a star with triangle ",
        }
    ],
    model="llama3-70b-8192",
)

print(chat_completion.choices[0].message.content)
