## Тестування часу "сердцебиття"
"""
<!-- 
Моніторингова система клєнта надсилає сигнал що вона працездатна кожні 30 сек. або менше.

Засобами автоматизації проаналізуйте наданий нам лог: ideas_for_test\heartbeat\hblog

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

Здається посилання на ПР з змінами одного файлу, всьо по класичному сценарію АЛЕ додатково приатачте лог, що сворить ваша робота. -->

"""
import re
from datetime import datetime
from datetime import timedelta
import logging
from pathlib import Path

def setup_logger() -> logging.Logger:
    """
    Sets up and returns the heartbeat logger.
    """
    log_file = Path(__file__).parent / "hb.log"
    logger = logging.getLogger("heartbeat_logger")
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:  # Prevent adding multiple handlers
        handler = logging.FileHandler(log_file, encoding="utf-8")
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

def read_log_file_line_by_line(file_path: str):
    """
    Generator that reads the log file line by line.
    """
    with open(file_path, encoding="utf-8") as f:
        for line in f:
            yield line.strip()

def parse_keys_and_timestamps(lines) -> dict:
    """
    Parses keys and timestamps from the log lines.
    """
    result = {}
    for line in lines:
        try:
            key_match = re.search(r"Key\s+([^\|\s]+)", line)
            ts_match = re.search(r"Timestamp\s+(\d{2}:\d{2}:\d{2})", line)
            if key_match and ts_match:
                key = key_match.group(1)
                timestamp = datetime.strptime(ts_match.group(1), "%H:%M:%S")
                result.setdefault(key, []).append(timestamp)
        except Exception as e:
            logger = logging.getLogger("heartbeat_logger")
            logger.error(f"Failed to parse line: {line}. Error: {e}")
            continue
    return result

def check_heartbeat_intervals(data: dict, logger: logging.Logger):
    """
    Checks heartbeat intervals and logs warnings or errors based on the time difference.
    """
    warning_threshold = timedelta(seconds=30)
    error_threshold = timedelta(seconds=32)

    for key, timestamps in data.items():
        timestamps.sort()
        for i in range(1, len(timestamps)):
            delta = timestamps[i] - timestamps[i-1]
            current_time_str = timestamps[i].strftime("%H:%M:%S")
            if delta > warning_threshold and delta < error_threshold:
                logger.warning(f"[{key}] at {current_time_str} Heartbeat {delta.total_seconds():.0f}s exceeds 30s threshold.")
            elif delta >= error_threshold:
                logger.error(f"[{key}] at {current_time_str} Heartbeat {delta.total_seconds():.0f}s exceeds 32s ERROR threshold!")

if __name__ == "__main__":
    logger = setup_logger()
    lines = read_log_file_line_by_line("lesson_20/hblog.txt")
    data = parse_keys_and_timestamps(lines)
    check_heartbeat_intervals(data, logger)
