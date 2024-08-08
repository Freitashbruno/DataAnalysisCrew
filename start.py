import os
import sys

# Configure o PYTHONPATH
sys.path.insert(0, os.path.abspath('src'))

# Execute o script principal
from data_analysis_crew.main import main

if __name__ == "__main__":
    main()
