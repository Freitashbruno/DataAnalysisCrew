from src.data_analysis_crew.crew import crew
import pandas as pd  # Importa a biblioteca pandas para salvar em CSV

if __name__ == "__main__":
    # Define os caminhos de entrada e saída
    inputs = {
        'file_path': 'path/to/your/data.csv',  # Caminho para o arquivo de dados
        'output_path': 'path/to/save/visualization.png'  # Caminho para salvar a visualização
    }

    # Executa a função principal da biblioteca crewai
    result = crew.kickoff(inputs=inputs)

    # Imprime os resultados no console
    print(result)

    # Converte os resultados (assumindo que seja um dicionário ou lista de dicionários) para um DataFrame pandas
    try:
        df_results = pd.DataFrame(result)
    except ValueError:
        print("Os resultados não puderam ser convertidos para um DataFrame. Verifique o formato dos dados.")
    else:
        # Salva os resultados em um arquivo CSV
        df_results.to_csv('resultados.csv', index=False)
        print("Resultados salvos em 'resultados.csv'")
