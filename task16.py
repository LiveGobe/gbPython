n = int(input())  # вводим количество элементов в массиве
a = list(map(int, input().split()))  # вводим массив чисел
x = int(input())  # вводим число, которое нужно подсчитать вхождения

count = 0  # инициализируем счетчик вхождений

for num in a:
    if num == x:
        count += 1

print(count)  # выводим количество вхождений числа x в массиве