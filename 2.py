numbers = [4,5,7,8,10]
a = int(input("Число: "))
b = int(input("Число: "))
if a in numbers and b in numbers:
    print("Оба числа есть!")
elif a in numbers or b in numbers:
    print("Одно из чисел есть")
else:
    print("Ни одного из чисел нет")