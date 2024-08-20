# src/data_analysis_crew/main.py
from src.data_analysis_crew.crew import crew 
# ... restante do código do arquivo main.py

if __name__ == "__main__":
    inputs = {
        'file_path': 'path/to/your/data.csv', 
        'output_path': 'path/to/save/visualization.png'
    }

    result = crew.kickoff(inputs=inputs)

    print(result)

    try:
        df_results = pd.DataFrame(result)
    except ValueError:
        print("Os resultados não puderam ser convertidos para um DataFrame. Verifique o formato dos dados.")
    else:
        df_results.to_csv('resultados.csv', index=False)
        print("Resultados salvos em 'resultados.csv'")
