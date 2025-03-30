from pathlib import Path
import logging
import csv
import json
import xml.etree.ElementTree as ET


def setup_logger(name: str, log_file: Path, level=logging.INFO) -> logging.Logger:
    """
    Створює та повертає логер із вказаним ім'ям, файлом та рівнем логування.

    :param name: Ім'я логера (унікальне для кожного завдання)
    :param log_file: Шлях до лог-файлу
    :param level: Рівень логування (за замовчуванням INFO)
    :return: Об'єкт логера
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Створюємо FileHandler
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    )

    # Додаємо хендлер до логера (перевіряємо, щоб не дублювати)
    if not logger.hasHandlers():
        logger.addHandler(file_handler)

    return logger


"""
Завдання 1:
Візміть два файли з теки ideas_for_test/work_with_csv порівняйте на наявність дублікатів і приберіть їх.
Результат запишіть у файл result_<your_second_name>.csv
"""


def read_csv(filepath: Path) -> set:
    """Зчитує CSV-файл і повертає множину унікальних рядків

    :param filepath: шлях до файлу, який необхідно прочитати
    :return: множину у виді кортежу"""
    with open(filepath, encoding="utf-8") as file:
        reader = csv.reader(file)
        return {tuple(row) for row in reader}


def write_csv(filepath: Path, data: set) -> None:
    """Записує унікальні значення у CSV-файл

    :param filepath: шлях до файлу, в який необхідно записати
    :return: нічого"""
    with open(filepath, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)


def remove_duplicates(file_1: Path, file_2: Path, output_file: Path) -> None:
    """Порівнює два CSV-файли та записує унікальні значення в новий файл

    :param file_1: шлях до першого файлу, який необхідно зрівняти
    :param file_2: шлях до другого файлу, який необхідно зрівняти
    :param output_file: шлях до файлу, в який будуть записані унікальні рядки з обох файлів
    :return: множину у виді кортежу"""
    data1 = read_csv(file_1)
    data2 = read_csv(file_2)
    unique_rows = (data1 | data2) - (data1 & data2)
    write_csv(output_file, unique_rows)


"""
Завдання 2:
Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json. результат для невалідного файлу 
виведіть через логер на рівні еррор у файл json__<your_second_name>.log
"""

log_file_task2 = Path(__file__).parent / "json.log"
json_logger = setup_logger("json_validator", log_file_task2, level=logging.ERROR)


def validate_json_files(folder: Path) -> None:
    """Перевіряє всі JSON-файли у папці та логує невалідні

    :param folder: шлях до першого папки в якій лежать всі json файли для перевірки
    :return: нічого
    """
    for json_file in folder.glob("*.json"):
        try:
            with open(json_file, encoding="utf-8") as file:
                json.load(file)
        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            json_logger.error(f"Файл {json_file.name} не є валідним JSON: {e}")


"""
Завдання 3:
Для файла ideas_for_test/work_with_xml/groups.xml створіть функцію пошуку по group/number і повернення значення 
timingExbytes/incoming результат виведіть у консоль через логер на рівні інфо
"""

log_file_task3 = Path(__file__).parent / "groups_search.log"
xml_logger = setup_logger("xml_search", log_file_task3, level=logging.INFO)


def find_all_timing_incoming(xml_path: Path) -> None:
    """Знаходить усі групи, які містять timingExbytes/incoming, і логує їх значення

    :param xml_path: шлях до файлу в якому відбувається пошук
    :return: нічого"""
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()

        found = False
        for group in root.findall("group"):
            number = group.find("number")
            if number is not None:
                group_number = number.text
                timing = group.find("timingExbytes")
                if timing is not None:
                    incoming = timing.find("incoming")
                    if incoming is not None:
                        found = True
                        result = f"Група {group_number}: incoming = {incoming.text}"
                        xml_logger.info(result)

        if not found:
            xml_logger.info("Жодна група не містить 'timingExbytes/incoming'.")

    except ET.ParseError as e:
        xml_logger.error(f"Помилка парсингу XML: {e}")

    except Exception as e:
        xml_logger.error(f"Невідома помилка: {e}")


if __name__ == "__main__":
    # Таск 1
    # Файли для обробки
    file_1 = Path(__file__).parent / "work_with_csv/r-m-c.csv"
    file_2 = Path(__file__).parent / "work_with_csv/rmc.csv"
    result_file = Path(__file__).parent / "result_rmc.csv"
    file_3 = Path(__file__).parent / "work_with_csv/random.csv"
    file_4 = Path(__file__).parent / "work_with_csv/random-michaels.csv"
    result_file2 = Path(__file__).parent / "result_random.csv"
    remove_duplicates(file_1, file_2, result_file)
    remove_duplicates(file_3, file_4, result_file2)

    # Таск 2
    json_folder = Path(__file__).parent / "work_with_json"
    validate_json_files(json_folder)

    # Таск 3
    xml_file = Path(__file__).parent / "work_with_xml/groups.xml"
    find_all_timing_incoming(xml_file)
