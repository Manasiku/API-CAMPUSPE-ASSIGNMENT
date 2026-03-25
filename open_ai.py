import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat_with_openai():
    print("=== OpenAI Chatbot ===")
    user_input = input("You: ")
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        print("OpenAI:", response.choices[0].message.content)
    except Exception as e:
        print(f"Error: {e}")

chat_with_openai()