import re
import os
from datetime import datetime
import logging

def analyze_heartbeat_log(input_log_path, output_log_path, key="Key TSTFEED0300|7E3E|0400"):
    
    logging.basicConfig(
        filename=output_log_path,
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filemode='w'
    )

    timestamp_pattern = re.compile(r'Timestamp (\d{2}:\d{2}:\d{2})')
    key_lines = []

    if not os.path.exists(input_log_path):
        print(f"Файл '{input_log_path}' не знайдено!")
        return  

    with open(input_log_path, 'r') as f:
        for line in f:
            if key in line:
                match = timestamp_pattern.search(line)
                if match:
                    ts_str = match.group(1)
                    ts = datetime.strptime(ts_str, "%H:%M:%S")
                    key_lines.append((ts, line.strip()))

    for i in range(1, len(key_lines)):
        prev_ts, _ = key_lines[i - 1]
        current_ts, current_line = key_lines[i]
        delta = (current_ts - prev_ts).total_seconds()

        
        if delta < 0:
            delta += 86400  

        if 31 < delta < 33:
            logging.warning(f"Heartbeat {delta:.1f} seconds: {current_line}")
        elif delta >= 33:
            logging.error(f"Heartbeat {delta:.1f} seconds: {current_line}")





if __name__ == "__main__":
    analyze_heartbeat_log("hblog.txt", "hb_test.log")
    