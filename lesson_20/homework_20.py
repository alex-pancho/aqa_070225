### Тестування часу "сердцебиття"
"""
Моніторингова система клєнта надсилає сигнал що вона працездатна кожні 30 сек. або менше.

Засобами автоматизації проаналізуйте наданий нам лог: hblog

Змініть заготовку - файл hb_proces.py так щоб був аналіз правилності вимог:
    для кожного випадку де hertbeat більше 30 сек але менше 32 логувало варнінг в файлік hb.log
    для кожного випадку де hertbeat більше рівно 32 логувало error в файлік hb.log

Необовязова частина, виклик для найтриваліших:

(на оцінку не впливає, на самоцінку - впливає)

Врахуйте, що моніторінгових процесів декілька і вони ідентифікуються по ключу наприклад:

    Key TSTFEED0300
    Key TSTFEED0240

це два різні процеси, відповідно, для пошуку наступного"удару" слід також враховувати ключ.

Подумайте, що завтра вам використовувати файл hb_proces.py для тестів багатьох файлів

Згадайте, що ми вчили про серіалізацію і генератори, може воно тут треба.

(а може ні і я вас залутую) (а може базу даних в пам'яті ???)

Здається посилання на ПР з змінами одного файлу, всьо по класичному сценарію АЛЕ додатково приатачте лог, що сворить ваша робота.
"""

import re
from datetime import datetime
import logging
from pathlib import Path


def setup_heartbeat_logger() -> logging.Logger:
    """
    Налаштовує логгер для моніторингу серцебиття.
    :return: Логгер для моніторингу серцебиття.
    """
    log_file = Path(__file__).parent / "hb.log"
    logger = logging.getLogger("heartbeat_logger")
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:  # Щоб не додавати хендлери повторно
        handler = logging.FileHandler(log_file)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger


def read_log_file(file_path) -> str:
    """
    Читає лог-файл та повертає його вміст.
    :param file_path: Шлях до лог-файлу.
    :type file_path: str
    :return: Вміст лог-файлу.
    """
    with open(file_path, encoding="utf-8") as f:
        content = f.read()
    return content


def parse_keys_and_timestamps(content: str) -> dict:
    """
    Парсить ключі та часові мітки з вмісту переданих даних.
    :param content: Дані, що містять ключі та часові мітки.
    :type content: str
    :return: Словник, де ключі - це ідентифікатори процесів, а значення - списки часових міток.
    """
    result = {}
    for line in content.splitlines():
        key_match = re.search(r"Key\s+([^\|\s]+)", line)
        ts_match = re.search(r"Timestamp\s+(\d{2}:\d{2}:\d{2})", line)
        if key_match and ts_match:
            key = key_match.group(1)
            timestamp = timestamp_to_datetime(ts_match.group(1))
            result.setdefault(key, []).append(timestamp)
    return result


def timestamp_to_datetime(timestamp: str) -> datetime:
    """
    Перетворює рядок з часовою міткою у об'єкт datetime.
    :param timestamp: Рядок з часовою міткою у форматі "HH:MM:SS".
    :type timestamp: str
    :return: Об'єкт datetime.
    """
    return datetime.strptime(timestamp, "%H:%M:%S")


def check_heartbeat_intervals(
    timestamps_dict: dict, logger: logging.Logger, warn_threshold=30, error_threshold=32
):
    """
    Перевіряє інтервали між часовими мітками для кожного ключа та логує попередження або помилки.

    Параметри:
        timestamps_dict (dict): Словник, де ключі - це ідентифікатори процесів (наприклад, 'TSTFEED0003'),
                                а значення - списки об'єктів datetime, що представляють часові мітки.
        logger (logging.Logger): Логгер для запису попереджень та помилок.
        warn_threshold (int, optional): Поріг (у секундах), перевищення якого логує попередження. За замовчуванням 30 секунд.
        error_threshold (int, optional): Поріг (у секундах), перевищення якого логує помилку. За замовчуванням 32 секунди.

    Опис роботи:
        - Для кожного ключа функція сортує часові мітки.
        - Обчислює різницю (delta) між послідовними часовими мітками.
        - Якщо delta перевищує `warn_threshold`, але менше `error_threshold`, логує попередження.
        - Якщо delta дорівнює або перевищує `error_threshold`, логує помилку.
        - Логи містять ключ, часову мітку та значення delta у секундах.

    Приклад логів:
        [TSTFEED0003] at 04:21:00 Heartbeat 31s exceeds 30s threshold.
        [TSTFEED0003] at 04:51:17 Heartbeat 35s exceeds 32s ERROR threshold!
    """
    for key, timestamps in timestamps_dict.items():
        sorted_ts = sorted(timestamps)  # Сортуємо, щоб порівнювати правильно
        for i in range(1, len(sorted_ts)):
            delta = (sorted_ts[i] - sorted_ts[i - 1]).total_seconds()
            time_str = sorted_ts[i].strftime("%H:%M:%S")
            if warn_threshold < delta < error_threshold:
                logger.warning(
                    f"[{key}] at {time_str} Heartbeat {delta:.0f}s exceeds 30s threshold."
                )
            elif delta >= error_threshold:
                logger.error(
                    f"[{key}] at {time_str} Heartbeat {delta:.0f}s exceeds 32s ERROR threshold!"
                )


if __name__ == "__main__":
    content = read_log_file("hblog.txt")
    dict_key_time = parse_keys_and_timestamps(content)
    check_heartbeat_intervals(dict_key_time, setup_heartbeat_logger())
