import sys
import os

# Adicione o caminho onde o utils.py está localizado
sys.path.append('/content/drive/MyDrive/DataAnalysisCrew')

# Agora, você pode importar a função
from utils import get_openai_api_key

# Utilize a função para obter a chave da API
openai_api_key = get_openai_api_key()
os.environ["OPENAI_API_KEY"] = openai_api_key  # Certifique-se de que a chave é atribuída aqui
os.environ["OPENAI_MODEL_NAME"] = 'gpt-3.5-turbo'

# Configure o PYTHONPATH
sys.path.insert(0, os.path.abspath('src'))

# Execute o script principal
from data_analysis_crew.main import main

if __name__ == "__main__":
    main()
