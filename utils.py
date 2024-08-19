import os

def get_openai_api_key():
    """
    Retorna a chave da API OpenAI a partir das variáveis de ambiente.
    Se a chave não estiver definida, retorna uma chave padrão.
    """
    return os.getenv("OPENAI_API_KEY", "sk-9haG6QV06wIFPIx1hZR3om5ZRMxhux67_9QezCmdTqT3BlbkFJtNhtbGvn7Re_mmir0KgL0IlhcYSOnABHdh0sDL82wA")
