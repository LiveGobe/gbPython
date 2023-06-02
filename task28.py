def sum(a, b):
    if b == 0:
        return a
    else:
        return sum(a + 1, b - 1)
        
a = int(input("Введите число A: "))
b = int(input("Введите число B: "))

result = sum(a, b)

print("Сумма:", result)