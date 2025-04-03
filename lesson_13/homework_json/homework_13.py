import json
from pathlib import Path
import logging


def read_json(path: Path):
    with open(path, 'r') as file:
        data = json.load(file)
    return data


logging.basicConfig(
    filename="json_hello.log",
    filemode='w',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == "__main__":
    json_files = ["localizations_en.json", "localizations_ru.json", "login.json", "swagger.json"]
    for file in json_files:
        json_path = Path(__file__).parent / file
        try:
            read_json(json_path)
        except json.JSONDecodeError as e:
            logging.error(f"Файл {file} невалідний, помилка:{e}")
        except PermissionError as e:
            logging.error(f"Немає прав доступу до файлу: {json}")
