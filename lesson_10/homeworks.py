def sum_numbers_in_list(string_list: list):
    """Повертає список сум чисел зі списку строк,
    які складаються з чисел, розділених комою."""
    result = []
    for line in string_list:
        try:
            # Робимо спліт строки, розділеною комою, конвертуємо в int
            numbers = list(map(int, line.split(',')))
            # Додаємо сумми елементів в список
            result.append(sum(numbers))
        except (ValueError, AttributeError, AssertionError):
            result.append(f"Error: Invalid data in '{line}'")
    return result

""" 
def init(self, first_name, last_name, age, avarage_score = 3):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age 
        self.avarage_score = avarage_score
    
def change_score(self, avarage_score):
        self.avarage_score = avarage_score + avarage_score * 0.1
        return self.avarage_score
"""
if __name__ == "__main__":
    output = sum_numbers_in_list(["1,2,3", "4/0,6", "asas7,8,9"])
    print(sum_numbers_in_list(["1,2,3", "asas7,8,9", "4,0,6"]))
    #student_1 = ("Petro", "Onsienko", 19, 4.5)
    #result = student_1.change_score()
    #print(student_1.first_name, student_1.last_name, student_1.age, student_1.avarage_score)
