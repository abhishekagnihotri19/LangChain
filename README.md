Chatbot Using OpenAI & Multiple LLMs (OpenAI & Ollama) with LangChain

📌 Overview
This project is a **conversational AI chatbot** built using the **LangChain framework**. It supports:
Single LLM Chatbot:** Powered by OpenAI.
Multi-LLM Chatbot:** Uses OpenAI & Ollama for diverse responses.

The chatbot enables dynamic interaction by leveraging **multiple Large Language Models (LLMs)** to improve response quality and versatility.



🚀 Features
✅ Supports multiple LLMs (OpenAI, Ollama, etc.).  
✅ Built with **LangChain** for easy integration.  
✅ **FastAPI Backend** for API communication.  
✅ **Streamlit UI** for user-friendly chat experience.  
✅ Handles **dynamic routing** to different models based on user requests.  
✅ Configurable API settings using `.env` file.  


🛠 Tech Stack
- **Python 3.10+**
- **LangChain**
- **OpenAI API** (for OpenAI GPT models)
- **Ollama** (for local models)
- **FastAPI** (Backend API)
- **Streamlit** (Frontend UI)
- **Uvicorn** (Server for FastAPI)
- **Requests** (API handling)

---

🔧 Installation & Setup
1️⃣ Clone the Repository
```bash
git clone https://github.com/abhishekagnihotri19/LangChain.git
cd LangChain
```

2️⃣ Set Up a Virtual Environment
```
conda activate myenv
```

3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

4️⃣ Set Up Environment Variables
Create a `.env` file and add your OpenAI API key:
```env
OPENAI_API_KEY="your-openai-api-key"
OLLAMA_API_URL="http://localhost:11434"
```


🚀 Running the Chatbot
1️⃣ Start the FastAPI Server
```bash
uvicorn api.app:app --host 0.0.0.0 --port 8000
```

2️⃣ Run the Streamlit UI
```bash
streamlit run chatbot/app.py
```

---

## 📡 API Endpoints
### **POST** `/chat/single`
Handles single LLM chatbot requests using OpenAI.
```json
{
  "model": "gpt-4",
  "message": "Hello! How are you?"
}
```

**POST** `/chat/multi`
Routes requests between OpenAI & Ollama based on user preference.
```json
{
  "model": "Ollama(model="llama3.2:latest")",
  "message": "Tell me a joke."
}



## 🙌 Acknowledgments
- **LangChain**: For enabling seamless LLM integration.
- **OpenAI & Ollama**: For providing powerful AI models.

### 🌟 Star the Repo if You Found It Useful! ⭐

