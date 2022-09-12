from src.eda.executor import execute
from src.utils.utils import create_output_paths, parse_config

if __name__ == "__main__":
    parse_config()
    create_output_paths()

    execute()
