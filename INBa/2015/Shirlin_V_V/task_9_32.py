#Задача 9. Вариант 32.
#Создайте игру, в которой компьютер выбирает какое-либо слово, а игрок должен его отгадать. 
#Компьютер сообщает игроку, сколько букв в слове, и дает пять попыток узнать, есть ли какая-либо
#буква в слове, причем программа может отвечать только "Да" и "Нет". 
#Вслед за тем игрок должен попробовать отгадать слово.


# Ширлин Вячеслав Викторович
# 29.04.16

import random

WORDS = ("стол" , "стул" , "ствол", "машина", "карты" , "больница" ,"дом")

word = random.choice(WORDS)
 
print("\t\Приветствуем!")
print("Даем вам 10 попыток для отгадки слова, которое загадал компьютер.")
print("У тебя есть возможность узнать, есть ли определенная буква в слове.Затем ты можешь сразу сказать слово.")
print("Поехали!")
print("\nКоличество букв в слове:", len(word))
 
tries = 10
letter = ()
while tries >= 1:
    letter = str(input("В этом слове есть буква: "))
    if letter not in word:
        tries -= 1
        print("\nК сожалению, этой буквы нет в слове!")
        print(" У вас осталось", tries, "попыток(ки)!")
    if letter in word:
        tries -= 1
        print("\nВы угадали, эта буква есть в слове!")
        print("У вас осталось", tries, "попыток(ки)!")
 

no_assumptions= "Нет предположений"
print("\nВаши 10 попытки исчерпаны, вы готовы угадать слово?")
print("Если вы сдались и не хотите продолжать, напишите'Нет предположений' .")
correct = (input("\nЭто слово: "))
 
while correct != word:
    print("Попробуйте еще раз!")
    correct = (input("\nЭто слово: "))
    if correct == word:
        print("\n Спасибо за игру! Вы выиграли!Поздравляю!")
    if correct == i_dont_know:
        print("\n Спасибо за игру!Очень жаль!Может стоит попробовать еще?")
        break
 
input("\nНажмите Enter для выхода")