"""Завдання 1:

Візміть два файли з теки ideas_for_test/work_with_csv порівняйте на наявність дублікатів і "
"приберіть їх. Результат запишіть у файл result_<your_second_name>.csv"
"""

import csv
import json
import xml.etree.ElementTree as ET
import logging
from pathlib import Path


def read_file(filepath: Path) -> list:
    with open(filepath, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        return list(reader)

def remove_duplicates(content: list) -> list:
    header, *rows = content 
    unique_rows = list(map(list, {tuple(row) for row in rows})) 
    return [header] + unique_rows 

def write_csv(filepath: Path, content: list):
    with open(filepath, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerows(content)

if __name__ == "__main__":
    input_csv = Path(__file__).parent / "r-m-c.csv"
    input_csv = Path(__file__).parent / "rmc.csv"
    output_csv = Path(__file__).parent / "result_Lisitsa.csv"
    
    content = read_file(input_csv)
    unique_content = remove_duplicates(content)
    write_csv(output_csv, unique_content)

"""Завдання 2:

Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json. 
результат для невалідного файлу виведіть через логер на рівні еррор у файл json__<your_second_name>.log
"""


def setup_logger():
    logger = logging.getLogger("json_validator")
    logger.setLevel(logging.ERROR)
    file_handler = logging.FileHandler("json__Lisitsa.log", mode='w', encoding='utf-8')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger

def read_file(filepath: Path) -> dict:
    with open(filepath, "r", encoding="utf-8") as file:
        try:
            content = json.load(file)
        except json.decoder.JSONDecodeError as e:
            logger.error(f"Файл {filepath} не є валідним JSON: {e}")
            content = ""
        return content

def write_json(filepath: Path, content: dict):
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(content, file, indent=4)

if __name__ == "__main__":
    logger = setup_logger()
    folder_path = Path("ideas_for_test/work_with_json")
    for json_file in folder_path.glob("*.json"):
        content = read_file(json_file)
        print(content, type(content))

"""Завдання 3:

Для файла ideas_for_test/work_with_xml/groups.xml створіть функцію пошуку по group/number і 
повернення значення timingExbytes/incoming результат виведіть у консоль через логер на рівні інфо
"""

def setup_logger():
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
    return logging.getLogger(__name__)

def find_incoming_by_number(xml_path, group_number):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    
    for group in root.findall('group'):
        number = group.find('number')
        if number is not None and number.text == str(group_number):
            timing_exbytes = group.find('timingExbytes')
            if timing_exbytes is not None:
                incoming = timing_exbytes.find('incoming')
                if incoming is not None:
                    logger.info(f"Group {group_number} incoming: {incoming.text}")
                    return incoming.text
                
    logger.info(f"Group {group_number} has no incoming value")
    return None

if __name__ == "__main__":
    logger = setup_logger()
    xml_path = Path("/Users/rostiklisitsa/Desktop/AQA/Hillel/aqa_070225/lesson_13/groups.xml") 
    find_incoming_by_number(xml_path, 2)