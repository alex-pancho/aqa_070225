import csv
import json
import logging
import xml.etree.ElementTree as ET
from pathlib import Path

"""Завдання 1:
Візміть два файли з теки ideas_for_test/work_with_csv порівняйте на наявність дублікатів і приберіть їх. 
Результат запишіть у файл result_<your_second_name>.csv"""

def combine_files_and_show_unique_items(filepath1: Path, filepath2: Path, filepath3: Path) -> None:
    """This function reads two CSV files, combines their data, removes duplicate rows, 
    and writes the unique rows to a new CSV file."""

    with open(filepath1, 'r', encoding='utf-8') as first_file, open(filepath2, 'r', encoding='utf-8') as second_file:
             reader1 = list(csv.reader(first_file))
             reader2 = list(csv.reader(second_file))
             combined_data = reader1 + reader2
             unique_list = []
             for item in combined_data:
                   if item not in unique_list:
                         unique_list.append(item)

    with open(filepath3, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file, delimiter=";") #quoting=csv.QUOTE_ALL
        writer.writerows(unique_list)

"""Завдання 2:

Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json. 
Pезультат для невалідного файлу виведіть через логер на рівні еррор у файл json__<your_second_name>.log"""

def validate_json(folderpath: Path) -> None:
    """Function validates all JSON files in the specified folder to check if they are valid JSON.\n
    If the file contains invalid JSON, an error message is logged."""

    # Створення логера
    logger = logging.getLogger(__name__)
    # Налаштування рівня логування
    logger.setLevel(logging.ERROR)
    # Створення обробника для запису в файл
    file_handler = logging.FileHandler('json_lazurkevych.log')
    # Налаштування рівня логування для обробника
    file_handler.setLevel(logging.ERROR)
    # Створення форматера для обробника
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    # Додавання обробника до логера
    logger.addHandler(file_handler)

    for filepath in folderpath.iterdir():
        if filepath.is_file() and filepath.suffix == '.json':
            try:
                with open(filepath, "r", encoding="utf-8") as file:
                    json.load(file)
            except json.JSONDecodeError as e:
                log_message = f'File {filepath.name} is invalid JSON. Error message: {e}'
                logger.error(log_message)

"""Завдання 3:
Для файла ideas_for_test/work_with_xml/groups.xml створіть функцію пошуку по group/number і 
повернення значення timingExbytes/incoming результат виведіть у консоль через логер на рівні інфо"""

def find_incoming_by_number(filepath: Path, search_number: int) -> None:
    """Searches for a group by its number in an XML file and logs the value of the 'timingExbytes/incoming' to console."""

    # Створення логера
    logger = logging.getLogger(__name__)
    # # Налаштування рівня логування
    logger.setLevel(logging.INFO)
    # # Створення обробника для виводу в stdout
    console_handler = logging.StreamHandler()
    # # Налаштування рівня логування для обробника
    console_handler.setLevel(logging.INFO)
    # # Створення форматера для обробника
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    # # Додавання обробника до логера
    logger.addHandler(console_handler)

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
    """Task 1"""
    first_csv = Path(__file__).parent / "work_with_csv" / "r-m-c.csv"
    second_csv = Path(__file__).parent / "work_with_csv" / "rmc.csv"
    # first_csv = Path(__file__).parent / "work_with_csv" / "random-michaels.csv"
    # second_csv = Path(__file__).parent / "work_with_csv" / "random.csv"
    result_csv = Path(__file__).parent / "result_lazurkevych.csv"
    combine_files_and_show_unique_items(first_csv, second_csv, result_csv)
    """Task 2"""
    json_dir = Path(__file__).parent / 'work_with_json'
    validate_json(json_dir)
    """Task 3"""
    xml_path = Path(__file__).parent / "work_with_xml" / "groups.xml"
    find_incoming_by_number(xml_path, 2)