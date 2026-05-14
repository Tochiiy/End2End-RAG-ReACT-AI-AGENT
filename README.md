# End-to-End LangChain AI Agent with RAG
live-link

https://huggingface.co/spaces/Tochiiy/End2End-RAG-ReACT-AI-AGENT

A powerful AI application built with LangChain that combines intelligent agents with Retrieval-Augmented Generation (RAG) capabilities. This application features a user-friendly Gradio interface and leverages advanced NLP models for information retrieval and processing.

## 🎯 Features

- **Intelligent Agent**: LangChain-powered agent with tool-calling capabilities
- **RAG (Retrieval-Augmented Generation)**: Hybrid search combining web search and document retrieval
- **Web Search Integration**: Real-time web search via Tavily API
- **Document Processing**: PDF parsing and semantic search with FAISS
- **User-Friendly UI**: Interactive Gradio interface for seamless interaction
- **OpenAI Integration**: LLM-powered responses with GPT models
- **Vector Embeddings**: HuggingFace sentence transformers for semantic understanding

## 🛠️ Tech Stack

- **LangChain** - Framework for building LLM applications
- **OpenAI** - Large Language Model (GPT)
- **Gradio** - Web UI framework
- **FAISS** - Vector similarity search
- **Tavily** - Web search API
- **HuggingFace** - Transformer models and embeddings
- **PyPDF** - PDF document processing

## 📋 Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Tavily API key (for web search features)
- Virtual environment (recommended)

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd End2End-langchain-W-Agent
```

### 2. Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

### 5. Run the Application

```bash
python main.py
```

The application will start a local Gradio server. Access it via your browser at the URL shown in the console (typically `http://localhost:7860`).

## 📁 Project Structure
## view live web on the link below

https://huggingface.co/spaces/Tochiiy/End2End-RAG-ReACT-AI-AGENT

End2End-langchain-W-Agent/
├── agent/
│   ├── agent.py          # Core agent logic
│   └── runner.py         # Agent execution runner
├── tools/
│   ├── rag_tool.py       # RAG implementation
│   └── search_tools.py   # Search functionality
├── config/
│   └── settings.py       # Configuration settings
├── rag/                  # RAG data storage
├── ui/
│   └── app.py            # Gradio UI interface
├── main.py               # Application entry point
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (not in repo)
└── venv/                 # Virtual environment (not in repo)
```
