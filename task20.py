def calculate_word_value(word):
    value = 0
    for letter in word:
        if letter in ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']:
            value += 1
        elif letter in ['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У']:
            value += 2
        elif letter in ['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я']:
            value += 3
        elif letter in ['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы']:
            value += 4
        elif letter in ['K', 'Ж', 'З', 'Х', 'Ц', 'Ч']:
            value += 5
        elif letter in ['J', 'X', 'Ш', 'Э', 'Ю']:
            value += 8
        elif letter in ['Q', 'Z', 'Ф', 'Щ', 'Ъ']:
            value += 10
    return value

word = input("Введите слово: ")
word = word.upper()  # преобразуем слово в верхний регистр
value = calculate_word_value(word)
print("Стоимость слова:", value)