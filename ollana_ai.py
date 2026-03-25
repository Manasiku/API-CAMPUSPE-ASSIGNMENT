import requests

def chat_with_ollama():
    print("=== Ollama Chatbot (runs locally) ===")
    user_input = input("You: ")
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "llama3.2", "prompt": user_input, "stream": False}
        )
        data = response.json()
        print("Ollama:", data["response"])
    except Exception as e:
        print(f"Error: {e} — Make sure Ollama is running (run 'ollama serve' in terminal)")

chat_with_ollama()