from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI

LOCAL_DEEPSEEK_MODEL = ChatOpenAI(
    model='deepseek-r1',  # 选择本地 Ollama 模型
    base_url='http://localhost:11434/v1'  # 指向 Ollama 本地 API
)


LOCAL_LLAMA_MODEL = ChatOllama(
    model='llama3.2'
)

LOCAL_GEMMA_MODEL = ChatOllama(
    model='gemma3'
)