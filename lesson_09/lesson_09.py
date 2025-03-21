

class Car:
    #engine_on = False

    def __init__(self, brand, model, wheels=4):
        self.brand = brand
        self.model = model
        self.wheels = wheels
        self.engine_on = False # equal 4 str
        if wheels != 4:
            self.engine_key()
    
    def engine_key(self):
        print("Зміна стану двигуна викликана")
        self.engine_on = not self.engine_on
    
    def wrum(self):
        print("Wru-u-u-u-mm")


class Animal:

    def __init__(self):
        self.legs = 4
        # інкапсуляція
        self.__name = ""

    def birth(self):
        print("This animal gives birth")  # Виправлено повідомлення та додано self

    def speak(self):
        pass  # Загальний метод для всіх тварин

    def get_name(self):
        return self.__name

    def set_name(self, name):

        if not isinstance(name, str):
            raise ValueError("Use str here")
        
        self.__name = name


class Dog(Animal):
    # поліморфізм
    def speak(self):
        return "Гав!"  # Собака видає свій власний звук

class Cat(Animal):

    def __init__(self):
        #self.legs = 3
        pass

    def speak(self):
        return "Мяу!"  # Кіт також має свій власний звук

      
class BankAccount:

    def __init__(self, initial_balance):
        # інкапсуляція
        self.__balance = initial_balance  # Тут два знаки підкреслення позначають прихований атрибут

    def get_balance(self):
        return self.__balance

    def set_balance(self, value):
        if isinstance(value, (int, float)):  # Перевіряємо, чи є value числом
            self.__balance = value
        else:
            raise ValueError("Баланс повинен бути числом")  # Викидаємо помилку, якщо value не число


class People:

    def __init__(self, name):
        self.legs = 2
        # інкапсуляція
        self.__name = ""
        self.set_name(name)

   
    def get_name(self):
        return self.__name

    def set_name(self, name):

        if not isinstance(name, str):
            raise ValueError("Use str here")
        
        self.__name = name


class Printer():

    def __init__(self, name:str):
        self.name = name
    
    def to_print(self, data:str):
        print(data)
    
    def check_paper(self, counter:int):
        return counter > 0


class Scanner():

    def scan(self, some_string:str):
        self.copy = some_string
    
    # def to_print(self): # для методів з однак. ім'ям
    #     pass
  
class MFU(Printer, Scanner):
    
    def __init__(self, name):
        super().__init__(name)

if __name__ == "__main__":
    toyota = Car("Toyota", "Corolla", 3)
    mersedes = Car("Mesedes", "Benz")

    print(type(toyota), toyota.brand, toyota.model, toyota.wheels)
    print(type(mersedes), mersedes.brand, mersedes.model, mersedes.wheels)
    print("Поч", toyota.engine_on) 
    toyota.engine_key()
    print("Кін", toyota.engine_on)
    print("Мерс двиг", mersedes.engine_on)

    bingo = Dog()
    print(bingo.birth())
    bingo.set_name("Bingo")
    print(bingo.get_name())
    nemo = Animal()
    nemo.set_name("Nemo")
    print(nemo.get_name())
    nemo.__name = "Guppi"
    print(nemo.get_name())
    # nemo.set_name(1)
    account = BankAccount(1000)
    print(account.get_balance())  # Ми можемо отримати доступ до балансу через метод, а не прямо

    # Приклад зміни балансу
    account.set_balance(1500)
    print(account.get_balance())  # Виведе 1500

    # Спроба встановити нечислове значення
    try:
        account.set_balance("не число")  # Викличе помилку
    except ValueError as e:
        print(e)  # Виведе повідомлення про помилку
    
    arnold = People("Arni")
    print(arnold.get_name())

    hp_color = MFU("HP Color Jet")
    hp_color.to_print("Hello")

    bently = Car(wheels=5, model="Royal", brand="Bently")
    print(bently.brand, bently.model, bently.wheels)
