from langchain_ollama import OllamaLLM

def load_llm():
    llm=OllamaLLM(
        model="llama3",
        temperature=0
    )
    return llm