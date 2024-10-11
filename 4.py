numbers_1 = [1, 2, 3, 4, 5, 6, 7]
numbers_2 = [8, 9, 10, 11, 12]
a = sum(numbers_1)
b = sum(numbers_2)
if a > b:
    print("Первое среднее больше")
elif a < b:
    print("Второе среднее больше")
else:
    print("Средние одинаковые")
