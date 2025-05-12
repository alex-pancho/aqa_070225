"""### Тестування часу "сердцебиття"

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

""" Тестування часу "сердцебиття"

``Моніторингова система клєнта надсилає сигнал що вона працездатна кожні 30 сек. або менше.

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

Здається посилання на ПР з змінами одного файлу, всьо по класичному сценарію АЛЕ додатково приатачте лог, що сворить ваша робота."""

import logging
from datetime import datetime
from datetime import date
from datetime import timedelta
from pathlib import Path

logging.basicConfig(
    filename = Path(__file__).parent / 'hb_test.log',
    format = '%(asctime)s + %(levelname)s + %(message)s',
    level = logging.DEBUG,
    encoding='utf-8'
    )

logger = logging.getLogger()

def is_diff_31_33_sec(time_current:datetime, time_previous:datetime):
	# Обчислення різниці у часі
    time_difference = time_current - time_previous  
    # повертаємо True, якщо різниця 31-33 секунди
    return time_difference > timedelta(seconds=30) and time_difference <= timedelta(seconds=33)
       
    
def is_diff_more_33_sec(time_current:datetime, time_previous:datetime):
	# Обчислення різниці у часі
    time_difference = time_current - time_previous
    # повертаємо True, якщо різниця більше 33 секунди
    return time_difference > timedelta(seconds=33)
    
def filtered_log_record(filepath, key):
    #фільтруємо логи за ключем
    with open (f"{filepath}",  'r', encoding='utf-8') as f:
        log_list  = f.readlines()
    for log_element in log_list:
        if key in log_element:
            yield log_element

def heartbeat(filepath, key):
    #функція аналізує відфільтровані за ключем логи та записує результати в лог файл 
    later_record_time = None

    for log_record in filtered_log_record(filepath, key):
        position = log_record.find('Timestamp ')
        record_time = log_record[position+10:position+18]
        try:
            current_recor_time =  datetime.strptime(record_time, "%H:%M:%S")
        except Exception as e:
            logger.error(f"Не вдалося визначити час {log_record}, {e}")
            continue
            
        if later_record_time is not None:
            message = f"Time difference: {later_record_time - current_recor_time} at {record_time}"
            if is_diff_31_33_sec(later_record_time, current_recor_time):
                logger.warning(message)  
            elif is_diff_more_33_sec(later_record_time, current_recor_time):
                logger.error(message)
        later_record_time = current_recor_time
        

if __name__ == "__main__":
    
    filepath = Path(__file__).parent / "hblog.txt"
    key = "TSTFEED0300|7E3E|0400"
    heartbeat(filepath, key)