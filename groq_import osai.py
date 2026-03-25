import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def chat_with_groq():
    print("=== Groq Chatbot ===")
    user_input = input("You: ")
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": user_input}]
        )
        print("Groq:", response.choices[0].message.content)
    except Exception as e:
        print(f"Error: {e}")

chat_with_groq()