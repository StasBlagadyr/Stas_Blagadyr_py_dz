 #Доработать предыдущую функцию в num_translate_adv():
#реализовать корректную работу с числительными, начинающимися с заглавной буквы
eng_rus_num = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'}
def num_translate_adv(eng_word):
    if eng_word[0] == eng_word[0].upper():
        eng_word = eng_word.lower()
        return eng_rus_num[eng_word].capitalize()
    else:
        return eng_rus_num[eng_word]

print(num_translate_adv('Five'))
print(num_translate_adv('six'))
