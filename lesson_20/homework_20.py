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
from datetime import datetime

# Налаштування логування
logging.basicConfig(
    filename="hb_test.log",
    encoding="utf8",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def read_and_filter_log(filepath: str, key: str) -> list:
    """
    Читає файл і фільтрує рядки за заданим ключем.
    """
    filtered_lines = []
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            if key in line:
                filtered_lines.append(line.strip())
    return filtered_lines


def extract_timestamp(line: str) -> datetime:
    """
    Витягує об'єкт datetime з рядка за міткою Timestamp.
    """
    idx = line.find("Timestamp ")
    if idx != -1:
        time_str = line[idx + 10: idx + 18]
        return datetime.strptime(time_str, "%H:%M:%S")
    return None


def analyze_heartbeat(lines: list, key: str) -> None:
    """
    Аналізує heartbeat по відфільтрованих рядках.
    """
    timestamps = []

    for line in lines:
        ts = extract_timestamp(line)
        if ts:
            timestamps.append(ts)

    timestamps.sort()

    for i in range(len(timestamps) - 1):
        delta = (timestamps[i + 1] - timestamps[i]).total_seconds()
        time_of_error = timestamps[i + 1].strftime("%H:%M:%S")
        if 31 < delta < 33:
            logging.warning(f"{key} heartbeat warning: {delta:.0f} sec at {time_of_error}")
        elif delta >= 33:
            logging.error(f"{key} heartbeat error: {delta:.0f} sec at {time_of_error}")


if __name__ == "__main__":
    filepath = "hblog.txt"
    key = "Key TSTFEED0300|7E3E|0400"
    filtered_log = read_and_filter_log(filepath, key)
    analyze_heartbeat(filtered_log, key)
