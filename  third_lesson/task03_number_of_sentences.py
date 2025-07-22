# Задача 3
# Имате някакъв текст. Пребройте броя на изреченията в текста и изведете резултата на екрана.

text = input("Please enter text: ")
counter = 0

for letter in text:
    if ord(letter) == 46 or ord(letter) == 63 or ord(letter) == 33: # checking ., ?, !
        counter += 1

print(f"The number of sentences in the text is {counter}")