import logging
from datetime import datetime
from pathlib import Path
import re

# Настройка логирования
logging.basicConfig(
    filename='heartbeat_analyzer.log',
    filemode='w',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%H:%M:%S'
)

def parse_timestamp(line):
    match = re.search(r'Timestamp (\d{2}:\d{2}:\d{2})', line)
    if match:
        return datetime.strptime(match.group(1), "%H:%M:%S")
    return None

def parse_key(line):
    match = re.search(r'Key\s+(TSTFEED\d+)', line)
    if match:
        return match.group(1)
    return None

def heartbeat_log_generator(filepath):
    logging.info(f"Чтение файла: {filepath}")
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, 1):
                timestamp = parse_timestamp(line)
                key = parse_key(line)
                if key and timestamp:
                    yield key, timestamp, line.strip()
                else:
                    logging.debug(f"Пропущена строка {line_number} в {filepath}: {line.strip()}")
    except Exception as e:
        logging.error(f"Ошибка при чтении файла {filepath}: {e}")

def analyze_heartbeat(input_source, output_file):
    log_by_key = {}

    input_path = Path(input_source)
    if input_path.is_dir():
        files = list(input_path.glob('*'))
        logging.info(f"Найдено {len(files)} файлов в директории {input_source}")
    else:
        files = [input_path]
        logging.info(f"Обрабатывается одиночный файл: {input_source}")

    for filepath in files:
        if not filepath.is_file():
            logging.warning(f"Пропущен не-файл: {filepath}")
            continue
        for key, timestamp, line in heartbeat_log_generator(filepath):
            log_by_key.setdefault(key, []).append((timestamp, line))


    with open(output_file, 'w', encoding='utf-8') as out:
        for key, entries in log_by_key.items():
            entries.sort(key=lambda x: x[0])
            for i in range(len(entries) - 1):
                t1, _ = entries[i]
                t2, _ = entries[i + 1]
                delta = (t2 - t1).total_seconds()

                if delta < 0:
                    msg = f"Отрицательная дельта времени между {t1.strftime('%H:%M:%S')} и {t2.strftime('%H:%M:%S')} для ключа {key}"
                    logging.warning(msg)
                    continue

                if 31 < delta < 33:
                    msg = f"[{key}] {t1.strftime('%H:%M:%S')} → {t2.strftime('%H:%M:%S')} delta={delta:.2f} sec"
                    out.write("WARNING " + msg + '\n')
                    logging.warning(msg)
                elif delta >= 33:
                    msg = f"[{key}] {t1.strftime('%H:%M:%S')} → {t2.strftime('%H:%M:%S')} delta={delta:.2f} sec"
                    out.write("ERROR   " + msg + '\n')
                    logging.error(msg)

if __name__ == "__main__":
    input_path = "ideas_for_test/heartbeat/hblog"
    output_path = "hb_test.log"
    try:
        analyze_heartbeat(input_path, output_path)
        print(f"Готово. Результат у '{output_path}'")
        logging.info("Анализ завершён успешно.")
    except Exception as e:
        logging.critical(f"Критическая ошибка при выполнении: {e}")
