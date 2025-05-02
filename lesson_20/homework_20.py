import re
import logging
from datetime import timedelta, datetime

logger = logging.getLogger('HeartBeat')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file_handler = logging.FileHandler('heartbeat.log', mode='w')
filemode = 'w'
file_handler.setLevel(logging.WARNING)
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)


def extract_by_key(file_path, target_key):
    results = []

    pattern = re.compile(
        r"\{ Trade \((\d+), len \d+\) Queue \d+ PriceClass \d+ Timestamp ([\d:]+) Key (.*?) TradePrice (\d+) TradeSize (\d+) \}"
    )

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            match = pattern.search(line)
            if match:
                trade_id, timestamp, key, price, size = match.groups()
                if key == target_key:
                    results.append({
                        "TradeID": trade_id,
                        "Timestamp": timestamp,
                        "Key": key,
                        "TradePrice": int(price),
                        "TradeSize": int(size)
                    })

    return results


def check_and_log(data: list):
    for i, beat in enumerate(data):
        if i == 0:
            continue
        format_string = '%H:%M:%S'
        time1 = datetime.strptime(data[i]["Timestamp"], format_string)
        time2 = datetime.strptime(data[i - 1]["Timestamp"], format_string)
        timediff = time2 - time1
        if timedelta(seconds=33) >= timediff > timedelta(seconds=31):
            logger.warning(timediff)
        elif timedelta(seconds=33) < timediff:
            logger.error(timediff)


if __name__ == "__main__":
    file_path = "hblog.txt"
    target_key = "TSTFEED0300|7E3E|0400"
    matches = extract_by_key(file_path, target_key)
    check_and_log(matches)