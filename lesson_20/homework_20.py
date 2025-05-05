### Тестування часу "сердцебиття"
""" 
Моніторингова система клєнта надсилає сигнал що вона працездатна кожні 30 сек. або менше.

Засобами автоматизації проаналізуйте наданий нам лог: ideas_for_test\heartbeat\hblog

Змініть заготовку - файл hb_proces.py так щоб був аналіз правилності вимог:
    для кожного випадку де heartbeat більше 31 сек але менше рівно 33 логувало WARNING в файл hb_test.log
    для кожного випадку де heartbeat більше  33 логувало ERROR в файл hb_test.log

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

from datetime import datetime
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('hb_test.log')
logger.addHandler(file_handler)

def read_file(file_path):
    with open(file_path, 'r') as f: 
        return f.readlines()

def filter_heartbeat(lines):
    previous_time = None
    for line in lines:
            index = line.find("Timestamp ")
            if index != -1 and len(line) >= index + 18:
                timestamp = line[index + 10: index + 18]
                try:
                    current_time = datetime.strptime(timestamp, "%H:%M:%S")
                except ValueError:
                    logger.warning(f"Невірний формат часу: {timestamp} у рядку: {line.strip()}")
                    continue
            
                if previous_time:
                    delta_seconds = abs((current_time - previous_time).total_seconds())
                    
                    if 31 < delta_seconds <= 33:
                        logger.warning( f'WARNING - heartbeat = {delta_seconds} більше 31 сек але менше рівно 33 at {current_time}')
                    elif delta_seconds > 33:
                        logger.error(f'ERROR - heartbeat = {delta_seconds} більше 31 сек at {current_time}') 
            
                previous_time = current_time
            
def main():
    lines = read_file('/Users/andrewshevchenko/Vera_Project/hillel/aqa_070225/lesson_20/hblog.txt')
    filter_heartbeat(lines)
    
if __name__ == "__main__":
    main()
            
    

 
        
    

