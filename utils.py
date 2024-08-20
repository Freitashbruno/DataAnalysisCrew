import os

def get_openai_api_key():
    """
    Retorna a chave da API OpenAI a partir das variáveis de ambiente.
    Se a chave não estiver definida, retorna uma chave padrão.
    """
    return os.getenv("OPENAI_API_KEY", "sk-your-api-key-ending-in-DL82wA")
