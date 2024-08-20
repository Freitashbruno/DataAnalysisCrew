import sys
import os

# Adiciona o caminho onde o utils.py está localizado
sys.path.append('/content/drive/MyDrive/DataAnalysisCrew')

# Importa a função get_openai_api_key do utils.py
from utils import get_openai_api_key

# Obtém a chave da API OpenAI e define a variável de ambiente
openai_api_key = get_openai_api_key()
os.environ["OPENAI_API_KEY"] = openai_api_key  # Certifique-se de que a chave é atribuída corretamente aqui
os.environ["OPENAI_MODEL_NAME"] = 'gpt-3.5-turbo'

# Configura o PYTHONPATH para incluir o diretório src
sys.path.insert(0, os.path.abspath('src'))

# Importa e executa o script principal
from src.data_analysis_crew.main import main

if __name__ == "__main__":
    main()
