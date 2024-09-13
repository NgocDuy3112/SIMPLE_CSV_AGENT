from __init__ import *

def create_llm_from_ollama(model_name:str="gemma2") -> OllamaLLM:
    return OllamaLLM(model=model_name)

def create_huggingface_embedding_model(model_name:str="keepitreal/vietnamese-sbert") -> HuggingFaceEmbeddings:
    return HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs={'device': 'cpu'},
        encode_kwargs={'normalize_embeddings': False}
    )