# Завдання 2:
# Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json. 
# результат для невалідного файлу виведіть через логер на рівні еррор у файл json__<your_second_name>.log

"""
Validates all JSON files in 'work_with_json' folder.
Logs invalid files with error details to 'json__benedek.log'.
Run this script to check for broken JSON files.
"""

import logging
from pathlib import Path
import json

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

log_file = Path(__file__).parent.parent / "json__benedek.log"
file_handler = logging.FileHandler(log_file, encoding="utf-8")
file_handler.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def validate_json(file_path: Path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            json.load(f)
        return True
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON: {file_path.name} – {str(e)}")
        return False

if __name__ == "__main__":
    input_folder = Path(__file__).parent.parent / "work_with_json"

    for file in input_folder.iterdir():
        if file.is_file() and file.name.endswith(".json"):
            validate_json(file)


