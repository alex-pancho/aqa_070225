print("Task 6.1***********")
input_sting = input("Введіть довгу строку: ")
new_set = set(input_sting)
if len(new_set) >= 10:
    print ("True")
elif len(new_set) < 10:
    print("False")
else: 
    print("False")


print("Task 6.2***********")
while True:
    word = input("Введіть слово, яке містить літеру 'h'.")
    if "h" in word:
       print("Ви ввели праавильно слово", word)
       break
    else:
         print("Помилка! Слово не містить літери 'h'. Спробуйте ще раз.")
         


print("Task 6.3***********")
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []
for char in lst1:
    if type(char) == str:
        lst2.append(char)
print(lst2)