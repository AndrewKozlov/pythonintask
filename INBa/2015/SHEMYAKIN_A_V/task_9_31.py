# Задача 9. Вариант 31. 
# 1-50. Создайте игру, в которой компьютер выбирает какое-либо слово, а игрок должен его отгадать. Компьютер сообщает игроку, сколько букв в слове, и дает пять попыток узнать, есть ли какая-либо буква в слове, причем программа может отвечать только "Да" и "Нет". Вслед за тем игрок должен попробовать отгадать слово.
# Shemyakin A.V. 
# 29.05.2016

import random
slova = ("клавиатура", "доспех", "самолет", "корабль", "документ", "ракушка")
word = random.choice(slova)
tryes = 5
bukvi = len(word)
bukva = ""
slovo = ""

print("Компьютер выбрал слово и вам нужно его отгадать. ")
print("В этом слове", str(bukvi), "букв.")
print("У вас есть ", str(tryes), " попыток угадать букву")

while tryes > 0:
    bukva = input ("\nВведите букву: ")
    if bukva in list(word):
        print("Да.")
        tryes -= 1
    else:
        print("Нет.")
        tryes -= 1
if tryes <= 0:
    slovo = input("У вас закончились попытки. Попробуйте угадать слово: ")
    if slovo == word:
        print("Поздравляю! Вы угадали слово. ")
    else:
        print("К сожалению вы не угадали. ")
input("\nДля выхода нажмите Enter")
