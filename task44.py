import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

# Создаем массив one hot encoding
one_hot = []
for item in lst:
    if item == 'robot':
        one_hot.append([1, 0])
    else:
        one_hot.append([0, 1])

# Создаем DataFrame с one hot encoding
data = pd.DataFrame(one_hot, columns=['robot', 'human'])

# Выводим первые 5 строк DataFrame
print(data.head())