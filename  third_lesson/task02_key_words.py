# Задача 2
# Потребителят въвежда някакъв текст от клавиатурата,
# след което потребителят въвежда списък със запазени думи.
# Всички запазени думи в текста трябва да бъдат намерени и техният регистър да бъде променен на главни букви.
# Изведете променения текст на екрана.

def an_empty_string (input_string):
    if input_string == "":
        return False
    else:
        return True

def key_words (input_text, input_key_words):
    curr_key = " "
    for letter_text in input_text:
        for letter_key in input_key_words:
            if letter_text == letter_key:
                curr_key = letter_text
    return curr_key.upper()


curr_text = input("Please enter text: ")
while True:
    if not an_empty_string(curr_text):
        print("Please enter text: ")
        curr_text = input()
    else:
        break

curr_key_words = input("Please enter key words: ")
while True:
    if not an_empty_string(curr_key_words):
        print("Please enter key words: ")
        curr_key_words = input()
    else:
        break

curr_text_split = curr_text.split(" ")
curr_key_words_split = curr_key_words.split(" ")
new_text = ""
for word in curr_text_split:
    if word in curr_key_words_split:
        word = word.upper()
    new_text += f"{word} "

print(new_text)
