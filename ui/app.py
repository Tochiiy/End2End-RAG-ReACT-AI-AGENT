import gradio as gr
from agent.agent import build_agent
from agent.runner import retry
from rag.vectorstore import build_vectorstore

vectorstore = None
agent       = build_agent()

def upload_file(file):
    global vectorstore, agent
    vectorstore = build_vectorstore(file.name)
    agent       = build_agent(vectorstore)
    return "✅ Document loaded! Ask me any relevant questions."

def chat(message, history):
    return retry(agent, message)

def create_ui():
    with gr.Blocks(title="END2END Web🕸️RAG Agent") as AiApp:
        gr.Markdown("# 🤖 RAG Agent\nUpload a document and chat with it — or ask anything using web search.")

        with gr.Row():
            file_upload   = gr.File(label="Upload PDF or TXT", file_types=[".pdf", ".txt"])
            upload_status = gr.Textbox(label="Status", interactive=False)

        file_upload.change(upload_file, inputs=file_upload, outputs=upload_status)

        gr.ChatInterface(
            fn=chat,
            chatbot=gr.Chatbot(height=400),
            textbox=gr.Textbox(placeholder="Ask a question...", scale=7),
            examples=[
                "What is the main topic of the document?",
                "Latest AI news today?",
            ],
        )
    return AiApp