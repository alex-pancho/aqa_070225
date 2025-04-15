"""
Створіть клас геометричної фігури "Ромб". Клас повинен мати наступні атрибути:

    сторона_а (довжина сторони a).
    кут_а (кут між сторонами a і b).
    кут_б (суміжний з кутом кут_а).

Необхідно реалізувати наступні вимоги:

    Значення сторони сторона_а повинно бути більше 0.
    Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
    Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а, 
    значення кут_б обчислюється автоматично.
    Для встановлення значень атрибутів використовуйте метод __setattr__.
"""
class Rhombus():
    
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a
        
    def __setattr__(self, name, value):
        if name == "side_a":
            if value <= 0:
                raise ValueError("Неправильно заданa side_a, сторона а має бути > 0 ")
            super().__setattr__(name, value)
            
        elif name == "angle_a":
            if not (0 < value < 180):
                raise ValueError("Кут повинен бути в межах від 0 до 180") 
            super().__setattr__(name, value)
            super().__setattr__("angle_b", 180 - value)
        
        else:
            super().__setattr__(name, value)
  
    def __str__(self):
        return f"Ромб: сторона = {self.side_a}, кут А = {self.angle_a}, кут Б = {self.angle_b}"

if __name__ == "__main__":
    romb = Rhombus(10, 60)
    print(romb)

        
        
        


