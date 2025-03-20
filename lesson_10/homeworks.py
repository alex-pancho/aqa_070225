def sum_numbers_in_list(string_list: list):
    '''Повертає список сум чисел зі списку строк,
    які складаються з чисел, розділених комою.'''
    result = []
    #перевіряємо умову 5: якщо передано не список
    if not isinstance(string_list, list) :
        raise ValueError("Не список")
    #перевіряємо умову 4: якщо передано порожній список
    if len(string_list) == 0 :
        raise ValueError("Список порожній")
    # ітеруємо по елементах списку
    for item in string_list:
        #перевіряємо умову 3: якщо елемент списку не є рядком
        if not isinstance(item, str):
            result.append("Не можу це зробити! AttributeError")
            #якщо елемент не рядок, переходимо до наступного елемента string_list
            continue
        else:
            #якщо елемент рядок, робимо спробу виконати умову 1
            try:
                suma = 0
                splitted_string = item.split(",")
                for i in splitted_string:
                    suma += float(i)
                result.append(suma)
            #Якщо рядок містить некоректні символи, виконуємться умова 2
            except ValueError as e:
                result.append("Не можу це зробити!")
    return result

class Student:
    def __init__(self,first_name: str, last_name:str, age:float, gpa:float):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gpa = gpa

        #type/value check
        if not isinstance(first_name, str):
            raise ValueError("String is expected for first name") 
        if not isinstance(last_name, str):
            raise ValueError("String is expected for last name") 
        if not isinstance(age, (int, float)) or not (16 <= age <= 100):
            raise ValueError("Int or float in range 16-100 is expected for age") 
        if not isinstance(gpa, (int, float)) or not (0 <= gpa <= 100):
            raise ValueError("Int or float in range 0-100 is expected for GPA") 
        
         
    def change_gpa(self, new_gpa:float):
        """змінює середній бал студента"""
        if isinstance(new_gpa, (int, float)) and (0 <= new_gpa <= 100):
            self.gpa = new_gpa
        else:
            raise ValueError("Int or float in range 0-100 is expected for new GPA") 

    def print_info(self):
        print(f"Name: {self.first_name} {self.last_name} age: {self.age} gpa: {self.gpa}")

            
def average_of_list(list_of_numbers:list):
    ''' Oбчислює середнє арифметичне списку чисел'''
    #перевіряємо чи заданий список
    if not isinstance(list_of_numbers, list):
        raise ValueError("List is expected")
    #перевіряємо чи всі елементи списку не числа
    if all(not isinstance(list_element, (int, float)) for list_element in list_of_numbers):
         raise ValueError("List has no number elements")
    #перевіряємо чи список не порожній
    if len(list_of_numbers) == 0:
        raise ValueError("List is empty.At least one element is expected")   
    #Якщо всі елемети числа, обчислюємо середнє арифметичне списку чисел
    if all(isinstance(list_element, (int, float)) for list_element in list_of_numbers):
        result = round(((sum(list_of_numbers)/len(list_of_numbers))), 3)
        #Якщо є елемети числа та інші, обчислюємо середнє арифметичне списку чисел, пропускаємо елементи які не числа
    else:
        total_sum = 0
        count = 0
        for list_element in list_of_numbers:
            if isinstance(list_element, (int, float)):
                total_sum += list_element
                count += 1
        result = total_sum / count
    return result

def longest_word (list_of_words):
    "Повертає перше найдовше слово у списку"

    #перевіряємо чи заданий список
    if not isinstance(list_of_words, list):
        raise ValueError("List is expected")
    
    #перевіряємо чи список не порожній
    if len(list_of_words) == 0:
        raise ValueError("List is empty")
    
    # формуємо новий список з тільки стрінгових елементів, щоб виключити не стрінгових елементів списку
    list_of_words_str  = []
    for element in list_of_words:
        if isinstance(element, str):
            list_of_words_str.append(element)
    
    #перевіряємо чи стрінговий список не порожній
    if len(list_of_words_str) == 0:
        raise ValueError("There are no string elements in list")

    #перевіряємо чи є в списку стрінга >=1 символ
    word_present = False
    for element in list_of_words_str:
            if len(element)>=1:
                word_present = True
    if word_present == False:
        raise ValueError("There are no words")
    
    #Позначаємо перший елемент стрінгового списку як найдовше слово
    long_word = list_of_words_str[0]

    #Шукаємо найдовше слово
    for word in list_of_words_str:
        if len(word)> len(long_word):
            long_word = word
    return long_word