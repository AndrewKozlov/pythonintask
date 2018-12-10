# Задача 9. 
# Создайте игру, в которой компьютер выбирает какое-либо слово, а игрок должен его отгадать. 
# Компьютер сообщает игроку, сколько букв в слове, и дает пять попыток 
# узнать, есть ли какая-либо буква в слове, 
# причем программа может отвечать только "Да" и "Нет". 
# Вслед за тем игрок должен попробовать отгадать слово.

# Dubs A. E.
# 05.05.2016

import random

WORDS = ("погода" ,"зима" ,"лето", "солнце", "снег", "земля", "дождь", "осень", "листья")

word = random.choice(WORDS)

comp_variant_bukva = len(word)

my_bukva = ''


print ("Программа выбирает какое-либо слово. \n Компьютер сообщает игроку, сколько букв в слове, и дает пять попыток узнать, есть ли какая-либо буква в слове")
print (" \n Вы должны отгадать слово, в котором" , )

popitki = 0
while popitki < 5:
	my_bukva = input ('Ваша буква: ')
	popitki += 1

	if my_bukva in word :
		print ("Да")
	else:
		print ("Нет")


print ("\n У Вас закончились попытки")
my_variant_slova = input ("\n Попробуйте отгадать слово плолностью:")

if my_variant_slova == word:
	print ("Вы отгадали слово!")
else :
	print ("Ваша игра закончена! Вы не угадали слово!")

input ("\n\n Нажмите Enter для выхода")
