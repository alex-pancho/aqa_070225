import logging
from pathlib import Path
import csv
import json
import xml.etree.ElementTree as ET
from pathlib import Path

#  логер для запису в файл
file_logger = logging.getLogger("file_logger")
file_handler = logging.FileHandler(Path(__file__).parent / 'validation_log.log', encoding="utf8")
file_handler.setFormatter(logging.Formatter('%(asctime)s  - %(levelname)s - %(message)s'))
file_logger.addHandler(file_handler)
file_logger.setLevel(logging.INFO)

#  логер для виведення в консоль
console_logger = logging.getLogger("console_logger")
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter('%(asctime)s  - %(levelname)s - %(message)s'))
console_logger.addHandler(console_handler)
console_logger.setLevel(logging.INFO)

def log_invalid_file(file):
    #Логує невалідні файли на рівні ERROR
    file_logger.error(f"File {file} is not a valid json")

def log_valid_file(file):
    #Логує валідні файли на рівні INFO
    file_logger.info(f"File {file} is a valid json")

def read(file_path):
    #Зчитує csv файл та повертає список.
    with open(file_path, "r", encoding="utf-8",newline='') as file:
        reader = csv.reader(file)
        return list(reader)
    
def write(file_path, content):
    #записує контент в файл
    with open(file_path, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerows(content)

def compare(path_1, path_2, path_3, path_4):
    # порівнює два файли за адресою path_1, path_2, записує унікальні значення в файл за адресою path_3, а дубльовані в файл за path_4
    file_1 = read(path_1)
    file_2 = read(path_2)
    compared_content = []
    duplicated_content =[]
    for element in file_1 + file_2:
        if element not in compared_content:
            compared_content.append(element)
        else:
            duplicated_content.append(element)
    write(path_3, compared_content)
    write(path_4, duplicated_content)

def check_json(path_dir):
    #перевіряє чи валідний json
    path_dir = Path(path_dir)
    for file in path_dir.iterdir():
        try:
            data = json.loads(file.read_text(encoding="utf-8"))
            log_valid_file(file) #Логуємо валідні файли
            
        except json.JSONDecodeError:
            log_invalid_file(file) #Логуємо невалідні файли

def xml_search(xml_path):
#функцію пошуку по group/number і повернення значення timingExbytes/incoming результат виведіть у консоль через логер на рівні інфо   
    xml_path = Path(xml_path)
    tree = ET.parse(xml_path)
    root = tree.getroot()
    for group in root.findall('group'):
        number = group.find('number')
        timing_exbytes = group.find('timingExbytes')
        if timing_exbytes is not None:
            incoming = timing_exbytes.find('incoming')
            if incoming is not None:
                console_logger.info(f"Group {number.text}: incoming = {incoming.text}")
            else:
                console_logger.info(f"Group:  {number.text}, incoming: Не знайдено")

if __name__ == "__main__":
    path_1 = Path(__file__).parent / "random-michaels.csv"
    path_2 = Path(__file__).parent / "random.csv"
    path_3 = Path(__file__).parent / "сompared_file.csv"
    path_4 = Path(__file__).parent / "duplicated.csv"
    compare(path_1, path_2, path_3, path_4)
    path_dir = Path(__file__).parent /"work_with_json"
    check_json(path_dir)
    xml_path = Path(__file__).parent / "groups.xml"
    xml_search(xml_path)



