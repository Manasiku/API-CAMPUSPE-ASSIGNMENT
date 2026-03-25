import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def chat_with_gemini():
    print("=== Google Gemini Chatbot ===")
    user_input = input("You: ")
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(user_input)
        print("Gemini:", response.text)
    except Exception as e:
        print(f"Error: {e}")

chat_with_gemini()