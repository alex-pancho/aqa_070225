import unittest

data = {
    'person1': {'gender': 'Male', 'height': 175},
    'person2': {'gender': 'Female', 'height': 160},
    'person3': {'gender': 'Male', 'height': 180},
    'person4': {'gender': 'Male', 'height': 170},
    'person5': {'gender': 'Female', 'height': 165},
    'person6': {'gender': 'Male', 'height': 185},
    'person7': {'gender': 'Female', 'height': 155},
    'person8': {'gender': 'Male', 'height': 190},
    'person9': {'gender': 'Male', 'height': 180},
    'person10': {'gender': 'Female', 'height': 162},
}

data_no_gender = {
    'person1': {'gender': '', 'height': 175},
    'person2': {'gender': '', 'height': 180},
}


def average_height(data, gender=None):
    height_list_male = []
    height_list_female = []

    for person in data.values():
        if person['gender'] == 'Male':
            height_list_male.append(person['height'])
        elif person['gender'] == 'Female':
            height_list_female.append(person['height'])

    if gender == 'Male':
        if height_list_male:
            return sum(height_list_male) / len(height_list_male)
        else:
            raise ValueError("немає даних для 'Male'")
    elif gender == 'Female':
        if height_list_female:
            return sum(height_list_female) / len(height_list_female)
        else:
            raise ValueError("немає даних для 'Female'")
    else:
        all_heights = height_list_male + height_list_female
        if all_heights:
            return sum(all_heights) / len(all_heights)
        else:
            raise ValueError("немає даних для 'gender'")


class TestAverageHeight(unittest.TestCase):

    def test_01_average_height_males(self):
        """Перевірка на вірність розрахунку середнього зросту Чоловіків (Male)"""
        result = average_height(data, 'Male')
        self.assertEqual(result, 180.0)

    def test_02_average_height_females(self):
        """Перевірка на вірність розрахунку середнього зросту Жінок (Female)"""
        result = average_height(data, 'Female')
        self.assertEqual(result, 160.5)

    def test_03_average_height_all(self):
        """Перевірка на вірність розрахунку середнього зросту всіх, незалежно від статі"""
        result = average_height(data, )
        self.assertEqual(result, 172.2)

    def test_04_ValueError_female(self):
        """Перевірка виклику помилки ValueError, коли немає гендеру  female"""
        with self.assertRaises(ValueError):
            data_no_females = {
                'person1': {'gender': 'Male', 'height': 175},
                'person2': {'gender': 'Male', 'height': 180},
            }

            average_height(data_no_females, 'Female')

    def test_05_ValueError_male(self):
        """Перевірка виклику помилки ValueError, коли немає гендеру male"""
        with self.assertRaises(ValueError):
            data_no_males = {
                'person1': {'gender': 'Female', 'height': 175},
                'person2': {'gender': 'Female', 'height': 180},
            }

            average_height(data_no_males, 'Male')

    def test_06_ValueError_all(self):
        """Перевірка виклику помилки ValueError незалежно від гендеру"""
        with self.assertRaises(ValueError):
            data_no_gender = {
                'person1': {'gender': '', 'height': 175},
                'person2': {'gender': '', 'height': 180},
            }

            average_height(data_no_gender)

    def test_07_message_female(self):
        """Перевірка тексту помилки при ValueError, коли немає гендеру для female"""
        data_no_females = {
            'person1': {'gender': 'Male', 'height': 175},
            'person2': {'gender': 'Male', 'height': 180}
        }
        with self.assertRaises(ValueError) as context:
            average_height(data_no_females, 'Female')
        self.assertEqual(str(context.exception), "немає даних для 'Female'")

    def test_08_AttributeError(self):
        """Перевірка невалідного вводу"""
        with self.assertRaises(AttributeError):
            data_empty_set = {()}
            average_height(data_empty_set)


if __name__ == "__main__":
    unittest.main(verbosity=2)
    print(f"Середній зріст чоловіків = {average_height(data, 'Male')}")
    print(f"Середній зріст жінок = {average_height(data, 'Female')}")
    print(f" Середній зріст і чоловіків і жінок = {average_height(data)}")
