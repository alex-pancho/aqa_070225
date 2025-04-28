# Тестування часу "сердцебиття"
# Моніторингова система клєнта надсилає сигнал що вона працездатна кожні 30 сек. або менше.
# Засобами автоматизації проаналізуйте наданий нам лог: ideas_for_test\heartbeat\hblog
# Змініть заготовку - файл hb_proces.py так щоб був аналіз правилності вимог:
#     для кожного випадку де heartbeat більше 31 сек але менше рівно 33 логувало WARNING в файл hb_test.log
#     для кожного випадку де heartbeat більше  33 логувало ERROR в файл hb_test.log

# Необовязова частина, виклик для найтриваліших:
# (на оцінку не впливає, на самоцінку - впливає)
# Врахуйте, що моніторінгових процесів декілька і вони ідентифікуються по ключу наприклад:
#     Key TSTFEED0300
#     Key TSTFEED0240
# це два різні процеси, відповідно, для пошуку наступного"удару" слід також враховувати ключ.
# Подумайте, що завтра вам використовувати файл hb_proces.py для тестів багатьох файлів
# Згадайте, що ми вчили про серіалізацію і генератори, може воно тут треба.
# (а може ні і я вас залутую) (а може базу даних в пам'яті ???)
# Здається посилання на ПР з змінами одного файлу, всьо по класичному сценарію АЛЕ додатково приатачте лог, що сворить ваша робота. 

import logging
from datetime import datetime, timedelta
from pathlib import Path


logging.basicConfig(
    filename="hb_test.log",
    encoding="utf8",
    level=logging.DEBUG, 
    format='%(asctime)s - %(levelname)s - %(message)s',
)

def open_file_and_filter_by_key(filepath: str, key: str) -> list:
    """
    Reads a log file and returns all lines containing the specified key.

    Args:
        filepath (str): Path to the log file.
        key (str): The key to search for in each line.

    Returns:
        List: A list of lines from the file that contain the key.
    """
    with open(filepath, 'r') as f:
        lines = f.readlines()

    filtered_list_by_key = [] 

    for line in lines:
        if key in line:
            filtered_list_by_key.append(line)
    return filtered_list_by_key

def get_timestamp(line: str) -> datetime:
    """
    Extracts a timestamp from a log line.

    Args:
        line (str): A single line from the log file.

    Returns:
        datetime: Parsed datetime object.
    """
    if "Timestamp " in line:
        index = line.find("Timestamp ")
        time_str = line[index + 10:index + 18]
        return datetime.strptime(time_str, "%H:%M:%S")
    
def format_timedelta(delta_seconds: float) -> str:
    """
    Converts a time difference in seconds to a HH:MM:SS string.

    Args:
        delta_seconds (float): Time difference in seconds.

    Returns:
        str: Formatted time difference string.
    """
    delta = timedelta(seconds=delta_seconds)
    return str(delta)

def analyze_heartbeat(filtered_lines: list, key: str) -> None:
    """
    Analyzes filtered log lines and logs heartbeat warnings and errors
    based on time gaps between consecutive timestamps.

    Args:
        filtered_lines (List): List of log lines containing the target key.
        key (str): The key being monitored, included in log messages.
    """
    timestamps = []

    for line in filtered_lines:
        timestamp = get_timestamp(line)
        if timestamp:
            timestamps.append(timestamp)

    for i in range(len(timestamps) - 1):
        delta = (timestamps[i] - timestamps[i + 1]).total_seconds()
        time_of_event = timestamps[i].time()

        formatted_delta = format_timedelta(delta)

        if 31 < delta < 33:
            logging.warning(f"{key} heartbeat warning: {formatted_delta} sec at {time_of_event}")
        elif delta >= 33:
            logging.error(f"{key} heartbeat error: {formatted_delta} sec at {time_of_event}")

if __name__ == '__main__':
    filepath = 'lesson_20/hblog.txt'
    key = 'Key TSTFEED0300|7E3E|0400'
    filtered_lines = open_file_and_filter_by_key(filepath, key)
    analyze_heartbeat(filtered_lines, key)