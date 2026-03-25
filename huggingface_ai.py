import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("HF_API_KEY")
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"

def chat_with_huggingface():
    print("=== Hugging Face Chatbot ===")
    user_input = input("You: ")
    try:
        headers = {"Authorization": f"Bearer {API_KEY}"}
        payload = {"inputs": user_input}
        response = requests.post(API_URL, headers=headers, json=payload)
        data = response.json()
        if isinstance(data, list):
            print("HuggingFace:", data[0]["generated_text"])
        else:
            print("HuggingFace:", data)
    except Exception as e:
        print(f"Error: {e}")

chat_with_huggingface()