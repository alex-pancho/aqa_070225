def print_lyrics():
    """Друкує пісню"""
    print("Ой у лузі червона калина похилилася")
    print("Чогось наша славна Україна зажурилася")

print_lyrics()

def say_hello(name:str="Anonymus", greeting: str="Hello") -> str:
    """Its greeting func

    :param name: Name for geeting
    :return str: greeting string
    """
    return f"{greeting}, {name}!"

print(say_hello("Vadym"))
print(say_hello("Vira", "Вітаю"))
print(say_hello(greeting="Вітаю", name="Тетяна"))

print(say_hello())
print("*"*88)
def print_args(*args):
    for arg in args:
        print(arg)
print_args(1, "hello", )
print("*"*88)
print_args(1, "hello", 3.14, [1, 2, 3])

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print("*"*88)
print_kwargs(name="John", age=25, city="New York")

def print_args_and_kwargs(*args, **kwargs):
    for arg in args:
        print(arg)

    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Приклад виклику функції
print_args_and_kwargs(1, "hello", 3.14, name="John", age=25)

add = lambda a, b: a + b
print(add(1, 2))

square = lambda x: x**2
print(square(5))