import csv
import json
import xml.etree.ElementTree as ET
from l_13_csv import read_file, write_csv
from pathlib import Path
import logging
import  os

log_dir = Path(r"C:\Users\qdbp\Documents\Study\aqa_070225\lesson_13\logs")
log_dir.mkdir(parents=True, exist_ok=True)
log_json = log_dir / "json_dorokhin.log"

json_logger = logging.getLogger("json_logger")
json_logger.setLevel(logging.ERROR)
json_handler = logging.FileHandler(log_json, encoding="utf-8")
json_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
json_logger.addHandler(json_handler)


xml_logger = logging.getLogger("xml_logger")
xml_logger.setLevel(logging.INFO)
xml_handler = logging.StreamHandler()
xml_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
xml_logger.addHandler(xml_handler)


# Завдання 1:
def csv_duplic_rem(path_1: Path, path_2: Path) -> list:
    csv_1 = read_file(path_1) 
    csv_2 = read_file(path_2)
    unit_path = csv_1 + csv_2
    # new_path = set()
    # for row in unit_path:
    #     new_path.add(tuple(row))
    # clear_list = []
    # for line in set(unit_path):
    #     clear_list.append(list(line))
    return [list(line) for line in set(tuple(row) for row in unit_path)]


# Завдання 2:
def read_file_json(filepath: Path) -> dict | None:
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.decoder.JSONDecodeError as e:
        json_logger.error(f"JSONDecodeError у файлі {filepath.resolve()}: {e}")
        return None
    except Exception as e:
        json_logger.error(f"Помилка читання JSON {filepath.resolve()}: {e}")
        return None


def json_valid(json_path: list):
    for file_path in json_path:
        json_content = read_file_json(file_path)
        if json_content is None:
            json_logger.error(f"Файл невалідний: {file_path.resolve()}")


# Завдання 2:
def xml_find_group_number(xml_path: str, group_number: str):
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
        
        for group in root.findall(".//group"):
            number = group.find("number")
            if number is not None and number.text == group_number:
                find_group_number = group.find("timingExbytes/incoming")
                if find_group_number is not None:
                    logging.info(f"Значення incoming для group {group_number}: {find_group_number.text}")
                    return find_group_number.text
                else:
                    logging.info(f"Знячення incoming для group {group_number} не знайдено")
                    return None
        
        logging.info(f"Group {group_number} не знайдено в XML-файлі")
        return None
    
    except ET.ParseError:
        logging.error("Помилка парсингу XML файла")
    except FileNotFoundError:
        logging.error("XML файл не знайдено")
    except Exception as e:
        logging.error(f"Неочікувана помилка: {e}")





if __name__ == "__main__":
    root_path = Path(r"C:\Users\qdbp\Documents\Study\aqa_070225\lesson_13")
    csv_path_1 = root_path / "random-michaels.csv"
    csv_path_2 = root_path / "random.csv"
    json_path_1 = root_path / "localizations_en.json"
    json_path_2 = root_path / "localizations_ru.json"
    json_path_3 = root_path / "login.json"
    json_files = [json_path_1, json_path_2, json_path_3]
    result_path = root_path / "result_dorokhin.csv"
    xml_file = root_path / "groups.xml"
    
    write_csv(result_path, csv_duplic_rem(csv_path_1, csv_path_2))
    json_valid(json_files)
    xml_find_group_number(xml_file, "10")
