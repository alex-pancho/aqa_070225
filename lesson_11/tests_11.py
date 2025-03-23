import unittest
import re
from homework_11 import log_event

class TestLogEvent(unittest.TestCase):

    def test_1_log_event_success(self):
        """Тестування логування для успішного входу"""

        # REMEMBER  assertLogs дозволяє захоплювати повідомлення логу, що генеруються під час виконання коду всередині блоку with
        #           level='INFO' визначає, що потрібно захоплювати лише логи з рівнем INFO або вищим
        #           assertLogs захоплює лише повідомлення логу, а не весь формат, як це відбувається при записі в файл, дата/час не перехоплюється
        #           as log: Логи, що генеруються всередині блоку with, будуть захоплені і збережені в змінну log( тип list)
        #           log.output — це атрибут, який містить список, в якому кожен елемент є рядком (string), що містить текст повідомлення логу, яке було згенеровано під час виконання коду в блоці with.
        
        with self.assertLogs(level='INFO') as log:     
            log_event('user1', 'success')
            # Перевіряємо, чи є в логах повідомлення з 'success'
            self.assertIn('Login event - Username: user1, Status: success', log.output[0])

    def test_2_log_event_expired(self):
        """Тестування логування для застарілого пароля"""
        with self.assertLogs(level='WARNING') as log:
            log_event('user2', 'expired')
            # Перевіряємо, чи є в логах повідомлення з 'success'
            self.assertIn('Login event - Username: user2, Status: expired', log.output[0])
  
    def test_3_log_event_error(self):
        """Тестування логування для невірного пароля"""
        with self.assertLogs(level="ERROR") as log:
            log_event('user3', 'failed')
            self.assertIn('Login event - Username: user3, Status: failed', log.output[0])

    def test_4_log_event_unknown_status(self):
        """Тестування логування для невідомого статусу"""
        with self.assertLogs(level="ERROR") as log:
            log_event('user3', "Success")  #capitalized is unknown
            self.assertIn('Login event - Username: user3, Status: Success', log.output[0])    

    def test_5_log_event_empty_str_username(self):
        """Тестування логування для empty_str_username"""
        with self.assertLogs(level="INFO") as log:
            log_event('', "success")  #capitalized is unknown
            self.assertIn('Login event - Username: , Status: success', log.output[0])  
 
   
        
        """ REMEMBER: Регулярні вирази (regular expressions або regex) — це інструмент для пошуку, перевірки, заміни та обробки тексту за допомогою шаблонів.
                      дозволяють створювати шаблони, які можна використовувати для пошуку в текстах рядків, перевірки їх відповідності певним умовам,а також виконувати заміни або інші операції.
                      Регулярні вирази використовують спеціальні символи для визначення шаблонів пошуку.
                        \d - відповідає будь-якій цифрі (еквівалентно [0-9]).
                        {n} — рівно n повторень (наприклад, a{3} шукає три символи a).
                        e.g Регулярний вираз для перевірки email-адреси: r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
                            ^:Це маркер початку рядка.
                            [a-zA-Z0-9._%+-]+:Це клас символів, який визначає, що перед символом @ в електронній пошті можуть бути задані символи
                            символ + після квадратних дужок означає, що один або більше таких символів повинно бути перед символом @. 
                            @ Це символ, який обов'язково має бути присутнім у кожній електронній пошті, він розділяє ім'я користувача та доменну частину.
                            [a-zA-Z0-9.-]+:Це знову клас символів, який визначає можливі символи для доменної частини електронної пошти після символу @
                            Символ + після квадратних дужок означає, що доменна частина має складатися хоча б з одного символу цього типу.
                            \.:Це ескейпований символ крапки. У регулярних виразах крапка . за замовчуванням означає будь-який символ, 
                               тому для того, щоб використати її як звичайну крапку, потрібно попередити її зворотним слешем (\.).
                            [a-zA-Z]{2,}:Це клас символів, який визначає домен верхнього рівня (TLD). Він повинен складатися зa-zA-Z — будь-яка велика або мала літера.
                            {2,} — кількість символів, яка має бути не меншою ніж два (для, наприклад, .com, .org та інші).
                            $ - Це маркер кінця рядка.
 
                      функцій для роботи з шаблонами регулярних виразів:
                        re.match() - перевіряє збіг лише на початку рядка. Повертає об'єкт класу MatchObject, якщо рядок знайдений, чи None, якщо не знайдений
                        re.search() - шукає відповідність у всьому рядку.
                        re.findall() - Знаходить усі збіги в рядку та повертає їх у вигляді списку.
                        re.sub() - Замінює збіги в рядку вказаною заміною.
        """
    def test_6_date_format(self):
        """Тестування формату дати"""
        with open('login_system.log', 'r') as log_file:
            log_content = log_file.readlines()
            self.assertGreater(len(log_content), 0, "Log file is empty")

            #date_format=r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}"
            date_format=r"[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]{3}"
            #якщо формат правильний, є збіг, в  match запишеться обєкт, якщо ні None
            match = re.match(date_format, log_content[-1]) #
            # Перевіряємо, що час виявлений і у правильному форматі
            self.assertIsNotNone(match, "Wrong format")
        

if __name__ == "__main__":
    unittest.main(verbosity=2)