# Завдання 3:
# Для файла ideas_for_test/work_with_xml/groups.xml створіть функцію пошуку по group/number 
# і повернення значення timingExbytes/incoming результат виведіть у консоль через логер на рівні інфо

"""
This script parses an XML file and logs the value of <timingExbytes>/<incoming> 
for each <group> by its <number>. If these elements are missing, it logs a message.
"""

import logging
import xml.etree.ElementTree as ET
from pathlib import Path

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

log_file = Path(__file__).parent.parent / "xml_info.log"
log_file.parent.mkdir(parents=True, exist_ok=True)

file_handler = logging.FileHandler(log_file, encoding="utf-8")
file_handler.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))
logger.addHandler(file_handler)

console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))
logger.addHandler(console_handler)

xml_path = Path(__file__).parent.parent / "work_with_xml" / "groups.xml"

def find_group_info(file_path: Path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        for group in root.findall("group"):
            number = group.find("number")
            incoming = group.find("timingExbytes/incoming")

            if number is not None and incoming is not None:
                logger.info(f"group {number.text} – incoming: {incoming.text}")
            else:
                logger.info("Could not find <number> or <incoming> in one of the groups")

    except FileNotFoundError:
        logger.error(f"XML file not found: {file_path}")
    except ET.ParseError as e:
        logger.error(f"XML parse error: {str(e)}")

if __name__ == "__main__":
    find_group_info(xml_path)
