from typing import Any, List, Dict
import csv
import json
import logging
from pathlib import Path
import xml.etree.ElementTree as ET

def setup_logger(log_filename: str, level=logging.INFO) -> logging.Logger:
    logger = logging.getLogger(log_filename)
    logger.setLevel(level)
    file_handler = logging.FileHandler(log_filename, mode='a', encoding='utf-8')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger


def read_file(filepath: Path, file_type: str) -> Any:
    if not filepath.exists():
        print(f"File {filepath} not found!")
        return None
    
    if file_type == 'csv':
        with open(filepath, "r", encoding="utf8") as file:
            reader = csv.reader(file, delimiter=";")
            return list(reader)
    
    elif file_type == 'json':
        with open(filepath, "r", encoding="utf8") as file:
            try:
                return json.load(file)
            except json.decoder.JSONDecodeError:
                return None
    
    elif file_type == 'xml':
        try:
            tree = ET.parse(filepath)
            return tree.getroot()
        except ET.ParseError:
            return None

def write_file(filepath: Path, content: Any, file_type: str):
    if content is None:
        print(f"No content to write to {filepath}")
        return
    
    if file_type == 'csv' and isinstance(content, list):
        with open(filepath, "w", encoding="utf8", newline="") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerows(content)
    
    elif file_type == 'json' and isinstance(content, dict):
        with open(filepath, "w", encoding="utf8") as file:
            json.dump(content, file, indent=4)

def remove_duplicates(content: list) -> list:
    if not content:
        return []
    header, *rows = content
    unique_rows = list(map(list, {tuple(row) for row in rows}))
    return [header] + unique_rows

def search_group_number(root, group_number: str, logger: logging.Logger):
    for group in root.findall(".//group"):
        if (number := group.find("number")) is not None and number.text == group_number:
            if (incoming := group.find("timingExbytes/incoming")) is not None:
                msg = f'Group {group_number}: Incoming timingExbytes = {incoming.text}'
            else:
                msg = f'Group {group_number} found, but no incoming timingExbytes'
            logger.info(msg)
            print(msg)
            return incoming.text if incoming is not None else None

    msg = f'Group {group_number} not found in XML'
    logger.info(msg)
    print(msg)
    return None

if __name__ == "__main__":
    """
    Завдання 1:
    Візміть два файли з теки ideas_for_test/work_with_csv порівняйте на наявність дублікатів "
    "і приберіть їх. Результат запишіть у файл result_<your_second_name>.csv
    """

    first_csv = Path("work_with_csv/rmc.csv")
    second_csv = Path("work_with_csv/r-m-c.csv")
    result_csv = Path("result_Anchyshyn.csv")

    content1 = read_file(first_csv, 'csv')
    content2 = read_file(second_csv, 'csv')

    if content1 and content2:
        combined_content = [content1[0]] + content1[1:] + content2[1:]
        unique_content = remove_duplicates(combined_content)
        write_file(result_csv, unique_content, 'csv')

    """
    Завдання 2:
    Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json. 
    результат для невалідного файлу виведіть через логер на рівні еррор у файл json__<your_second_name>.log
    """
    json_logger = setup_logger("json__Anchyshyn.log", logging.ERROR)
    folder_path = Path("work_with_json")

    for json_file in folder_path.glob("*.json"):
        content = read_file(json_file, 'json')
        if content is not None:
            print(f"Valid JSON: {json_file}")
        else:
            json_logger.error(f"Invalid JSON file: {json_file}")

    """
    Завдання 3:
    Для файла ideas_for_test/work_with_xml/groups.xml створіть функцію пошуку по group/number і 
    овернення значення timingExbytes/incoming результат виведіть у консоль через логер на рівні інфо
    """
    
    xml_logger = setup_logger("xml__Anchyshyn.log", logging.INFO)
    xml_file = Path("work_with_xml/groups.xml")
    group_numbers = ["1", "2", "3", "4", "5"]

    for group_number in group_numbers:
        content = read_file(xml_file, 'xml')
        if content is not None:
            search_group_number(content, group_number, xml_logger)
        else:
            xml_logger.error(f"Error parsing XML file: {xml_file}")