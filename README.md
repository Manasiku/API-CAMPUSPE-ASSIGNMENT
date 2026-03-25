# AI API Integration Assignment

**Institution:** CampusPe | Tattva Code Labs  
**Course:** Generative AI  
**Mentor:** Jacob Dennis

This project integrates six different Generative AI APIs using Python. 
Each program accepts a user prompt, sends it to the respective AI provider, 
and displays the response with proper error handling.

---

## Project Structure
```
ai-api-integration/
├── openai_example.py
├── groq_example.py
├── ollama_example.py
├── huggingface_example.py
├── gemini_example.py
├── cohere_example.py
├── multi_api_query.py
├── requirements.txt
├── README.md
└── screenshots/
    ├── openai_output.png
    ├── groq_output.png
    ├── ollama_output.png
    ├── huggingface_output.png
    ├── gemini_output.png
    └── cohere_output.png
```

---

## APIs Used

| Program | Provider | 
|---------|----------|
| openai_example.py | OpenAI GPT |
| groq_example.py | Groq LLaMA |
| ollama_example.py | Ollama (Local) |
| huggingface_example.py | Hugging Face |
| gemini_example.py | Google Gemini |
| cohere_example.py | Cohere |

---

## How to Obtain API Keys

| Provider | Link |
|----------|------|
| OpenAI | https://platform.openai.com/api-keys |
| Groq | https://console.groq.com/ |
| Ollama | https://ollama.ai/ (no key needed) |
| Hugging Face | https://huggingface.co/settings/tokens |
| Google Gemini | https://makersuite.google.com/app/apikey |
| Cohere | https://dashboard.cohere.com/ |

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/ai-api-integration.git
cd ai-api-integration
```

### 2. Install required packages
```bash
pip install openai groq requests google-generativeai cohere python-dotenv
```

### 3. Set up environment variables
Create a `.env` file in the root folder and add your API keys:
```
OPENAI_API_KEY=your_openai_key_here
GROQ_API_KEY=your_groq_key_here
HUGGINGFACE_API_KEY=your_huggingface_key_here
GOOGLE_API_KEY=your_gemini_key_here
COHERE_API_KEY=your_cohere_key_here
```

### 4. For Ollama (local setup only)
```bash
# Download from https://ollama.ai
ollama pull llama3.2
ollama serve
```

---

## How to Run Each Program
```bash
python openai_example.py
python groq_example.py
python ollama_example.py
python huggingface_example.py
python gemini_example.py
python cohere_example.py
```

Each program will ask:
```
Enter your prompt:
```
Type any message and press Enter to get the AI response.

## Important Notes

- API keys are never hardcoded in the code
- All keys are stored using environment variables
- The `.env` file is listed in `.gitignore` and will never be pushed to GitHub
- Free tier limits apply — be mindful of API rate limits
