from crewai_tools import tool

@tool
def DataCollectionTool(parameters):
    """
    Ferramenta para coleta de dados.

    Esta função lê um arquivo CSV especificado e retorna os dados em formato JSON.

    Args:
        parameters (dict): Dicionário contendo o caminho para o arquivo CSV no campo 'file_path'.

    Returns:
        str: Dados do arquivo CSV em formato JSON.
    """
    import pandas as pd
    data = pd.read_csv(parameters['file_path'])
    return data.to_json()

@tool
def StatisticalAnalysisTool(parameters):
    """
    Ferramenta para análise estatística.

    Esta função recebe dados em formato JSON e retorna um resumo estatístico dos dados.

    Args:
        parameters (dict): Dicionário contendo os dados em formato JSON no campo 'data'.

    Returns:
        str: Resumo estatístico dos dados em formato JSON.
    """
    import pandas as pd
    data = pd.read_json(parameters['data'])
    summary = data.describe().to_json()
    return summary

@tool
def DataVisualizationTool(parameters):
    """
    Ferramenta para visualização de dados.

    Esta função cria uma visualização gráfica (gráfico de barras) dos dados fornecidos e salva a imagem em um arquivo.

    Args:
        parameters (dict): Dicionário contendo os dados em formato JSON no campo 'data' e o caminho para salvar a visualização no campo 'output_path'.

    Returns:
        str: Caminho onde a visualização foi salva.
    """
    import pandas as pd
    import matplotlib.pyplot as plt
    data = pd.read_json(parameters['data'])
    plot = data.plot(kind='bar')
    plt.savefig(parameters['output_path'])
    return f"Visualization saved to {parameters['output_path']}"
