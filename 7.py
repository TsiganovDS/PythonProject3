list = []
n= int(input("Размер: "))
for i in range(n):
    x = int(input(f"Число {i + 1}: "))
    list.append(x)
a = 0
print(list)
for x in list:
    if x < 0:
        a += 1
print(a)


