from src.data_analysis_crew.crew import crew


if __name__ == "__main__":
    inputs = {'file_path': 'path/to/your/data.csv', 'output_path': 'path/to/save/visualization.png'}
    result = crew.kickoff(inputs=inputs)
    print(result)
