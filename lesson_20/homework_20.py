from datetime import datetime, timedelta
from collections import defaultdict

def read_log_file(filename):
    """Зчитує лог-файл построково"""
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()

def extract_key_and_timestamp(line):
    """Витягує ключ і timestamp із рядка"""
    try:
        time_idx = line.find("Timestamp ")
        if time_idx == -1:
            return None, None

        timestamp_str = line[time_idx + len("Timestamp "): time_idx + len("Timestamp ") + 8]
        timestamp = datetime.strptime(timestamp_str, "%H:%M:%S")

        # Знаходимо ключ
        key_idx = line.find("Key ")
        if key_idx == -1:
            return None, None

        key_part = line[key_idx + len("Key "):]
        key = key_part.split()[0] 
        return key, timestamp

    except Exception:
        return None, None

def analyze_heartbeat(input_file, output_file):
    """Основна функція аналізу логу"""
    heartbeat_data = defaultdict(list)

    
    for line in read_log_file(input_file):
        key, timestamp = extract_key_and_timestamp(line)
        if key and timestamp:
            heartbeat_data[key].append((timestamp, line))

    
    with open(output_file, 'w') as log_file:
        for key, records in heartbeat_data.items():
            
            records.sort(key=lambda x: x[0])

            for i in range(len(records) - 1):
                time_current, line_current = records[i]
                time_next, line_next = records[i + 1]

                diff = (time_next - time_current).total_seconds()
                if diff < 0:
                    diff += 86400  

                if 31 < diff < 33:
                    log_file.write(f"WARNING {diff} seconds for {key} between {time_current.strftime('%H:%M:%S')} and {time_next.strftime('%H:%M:%S')}\n")
                elif diff >= 33:
                    log_file.write(f"ERROR {diff} seconds for {key} between {time_current.strftime('%H:%M:%S')} and {time_next.strftime('%H:%M:%S')}\n")

if __name__ == "__main__":
    analyze_heartbeat('lesson_20/hblog.txt', 'lesson_20/hb_test.log')

