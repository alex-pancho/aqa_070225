import logging
from datetime import datetime, timedelta
from pathlib import Path
from collections import defaultdict

class HeartbeatAnalyzer:
    def __init__(self, log_path: Path, output_log: Path):
        # Input and output log file path
        self.log_path = log_path
        self.output_log = output_log
        self.key_records = defaultdict(list) 

        # Logger setup
        self.logger = logging.getLogger("HeartbeatAnalyzerLogger")
        self.logger.setLevel(logging.DEBUG)

        # Clear existing handlers (avoid duplicates if reused)
        if self.logger.hasHandlers():
            self.logger.handlers.clear()

        handler = logging.FileHandler(self.output_log, encoding='utf-8')
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def parse_log(self):
        # Read log lines and extract timestamps by process key
        try:
            with open(self.log_path, 'r', encoding='utf-8') as f:
                for line in f:
                    if not line.strip():
                        continue  

                    # Extract timestamp
                    pos = line.find("Timestamp ")
                    if pos == -1:
                        continue
                    try:
                        time_str = line[pos + 10:pos + 18]
                        timestamp = datetime.strptime(time_str, "%H:%M:%S")
                    except ValueError:
                        continue

                    # Extract process key
                    key_pos = line.find("Key ")
                    if key_pos == -1:
                        continue
                    key = line[key_pos + 4:].split()[0]

                    self.key_records[key].append(timestamp)
        except Exception as e:
            self.logger.error(f"Error reading log file: {e}")

    def is_warning(self, current, previous):
        # Time difference is > 31 and <= 33
        return timedelta(seconds=31) < (current - previous) <= timedelta(seconds=33)

    def is_error(self, current, previous):
        # Time difference is > 33
        return (current - previous) > timedelta(seconds=33)

    def process_all_keys(self):
        # Analyze each process separately
        for key, timestamps in self.key_records.items():
            timestamps.sort()
            previous_time = None
            max_diff = timedelta(0)

            for current_time in timestamps:
                if previous_time:
                    diff = current_time - previous_time
                    msg = f"Key {key}: Time difference {diff.total_seconds():.2f} seconds at {current_time.time()}"

                    if self.is_warning(current_time, previous_time):
                        self.logger.warning(msg)
                    elif self.is_error(current_time, previous_time):
                        self.logger.error(msg)

                    if diff > max_diff:
                        max_diff = diff

                previous_time = current_time

            if max_diff > timedelta(0):
                self.logger.info(f"Key {key}: MAX heartbeat delay = {max_diff.total_seconds():.2f} seconds")
                print(f"Key {key}: MAX heartbeat delay = {max_diff.total_seconds():.2f} seconds")

    def run(self):
        self.parse_log()
        self.process_all_keys()


if __name__ == "__main__":
    
    base_dir = Path(__file__).resolve().parent

    log_file = base_dir / "hblog.txt"
    output_log = base_dir / "hb_test.log"

    analyzer = HeartbeatAnalyzer(log_path=log_file, output_log=output_log)
    analyzer.run()