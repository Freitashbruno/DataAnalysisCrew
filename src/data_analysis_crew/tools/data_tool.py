from crewai_tools import tool

@tool
def DataCollectionTool(parameters):
    # Implementação da ferramenta de coleta de dados
    # Exemplo: leitura de arquivos CSV
    import pandas as pd
    data = pd.read_csv(parameters['file_path'])
    return data.to_json()

@tool
def StatisticalAnalysisTool(parameters):
    # Implementação da ferramenta de análise estatística
    import pandas as pd
    data = pd.read_json(parameters['data'])
    summary = data.describe().to_json()
    return summary

@tool
def DataVisualizationTool(parameters):
    # Implementação da ferramenta de visualização de dados
    import pandas as pd
    import matplotlib.pyplot as plt
    data = pd.read_json(parameters['data'])
    plot = data.plot(kind='bar')
    plt.savefig(parameters['output_path'])
    return f"Visualization saved to {parameters['output_path']}"
