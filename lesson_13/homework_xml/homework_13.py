import xml.etree.ElementTree as ET
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s")  # Встановлюємо рівень логування
logger = logging.getLogger(__name__)


def check_incoming(num: int, file_name: str):
    tree = ET.parse(file_name)
    root = tree.getroot()
    for group in root.findall('group'):
        number = group.find('number')
        if number.text == str(num):
            timing_exbytes = group.find('timingExbytes')
            if timing_exbytes is not None:
                incoming = timing_exbytes.find('incoming')
                if incoming is not None and incoming.text:
                    logger.info(f"Знайдено incoming: {incoming.text}")
                else:
                    logger.info("incoming не має тексту або відсутній")


if __name__ == "__main__":
    num = 4
    file_name = 'groups.xml'
    check_incoming(num, file_name)
