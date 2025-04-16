"""

Ітератори:

    Реалізуйте ітератор для зворотного виведення елементів списку.
    Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.

"""


class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data)
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
    

class EvenNumbers:
    def __init__(self, N):
        self.N = N
        self.current = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.N:
            raise StopIteration
        result = self.current
        self.current += 2
        return result
    


            
        
if __name__ == "__main__":
    # numbers = [1,2,3,4,5
    # for num in ReverseIterator(numbers):
    #     print(num)
    # for num in EvenNumbers(5):
    #     print(num)
    
            
             
        
        

