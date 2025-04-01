import csv
import json
import logging
import xml.etree.ElementTree as ET
from pathlib import Path

"""Створення логгера"""


def create_logger(log_filename: str = None, log_level=logging.INFO):
    # Створення логера
    logger = logging.getLogger(__name__)
    #  рівень логування
    logger.setLevel(log_level)

    if log_filename:
        file_handler = logging.FileHandler(log_filename)
        file_handler.setLevel(logging.ERROR)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    if not log_filename:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger


"""Task 1: Візміть два файли з теки ideas_for_test/work_with_csv порівняйте на наявність дублікатів і приберіть їх.
Результат запишіть у файл result_<your_second_name>.csv"""


def unique_items(filepath1: Path, filepath2: Path, filepath3: Path) -> None:
    with open(filepath1, 'r', encoding='utf-8') as first_file, open(filepath2, 'r', encoding='utf-8') as second_file:
        reader1 = list(csv.reader(first_file))
        reader2 = list(csv.reader(second_file))
        combined_data = reader1 + reader2
        unique_list = []
        for item in combined_data:
            if item not in unique_list:
                unique_list.append(item)

    with open(filepath3, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerows(unique_list)


"""Task 2: Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json.
Pезультат для невалідного файлу виведіть через логер на рівні еррор у файл json__<your_second_name>.log"""


def validate_json(folderpath: Path) -> None:
    logger = create_logger(log_filename='json_lypnyk.log', log_level=logging.ERROR)

    for filepath in folderpath.iterdir():
        if filepath.is_file() and filepath.suffix == '.json':
            try:
                with open(filepath, "r", encoding="utf-8") as file:
                    json.load(file)
            except json.JSONDecodeError as e:
                log_message = f'File {filepath.name} is invalid JSON. Error message: {e}'
                logger.error(log_message)


"""Task 3: Для файла ideas_for_test/work_with_xml/groups.xml створіть функцію пошуку по group/number і
повернення значення timingExbytes/incoming результат виведіть у консоль через логер на рівні інфо"""


def find_incoming_by_number(filepath: Path, search_number: int) -> None:
    logger = create_logger(log_level=logging.INFO)

    tree = ET.parse(filepath)
    root = tree.getroot()

    for group in root.findall('group'):
        number = group.find('number').text
        if int(number) == search_number:
            timing_exbytes = group.find('timingExbytes')
            if timing_exbytes is not None:
                incoming = timing_exbytes.find('incoming')
                if incoming is not None:
                    log_message = f'Searched_number: {search_number}; incoming: {incoming.text}.'
                    logger.info(log_message)
                else:
                    log_message = (f'Error: \'incoming\' is None for searched number {search_number}.')
                    logger.info(log_message)
            else:
                log_message = (f'Error: \'timing_exbytes\' is None for searched number {search_number}.')
                logger.info(log_message)


if __name__ == "__main__":
    """Task 1 results: """
    first_csv = Path(__file__).parent / "work_with_csv" / "r-m-c.csv"
    second_csv = Path(__file__).parent / "work_with_csv" / "rmc.csv"
    result_csv = Path(__file__).parent / "result_lypnyk.csv"
    unique_items(first_csv, second_csv, result_csv)

    """Task 2 results: """
    json_dir = Path(__file__).parent / 'work_with_json'
    validate_json(json_dir)

    """Task 3 results: """
    xml_path = Path(__file__).parent / "work_with_xml" / "groups.xml"
    find_incoming_by_number(xml_path, 2)
