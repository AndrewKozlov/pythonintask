# Задача 6. Вариант 32
# Создайте игру, в которой компьютер загадывает название одного из двадцати восьми стран, входящих в Европейский союз, а игрок должен его угадать.
# 24.03.2016
# Ширлин Вячеслав Викторович

import random

print ("Программа загадывает название одного из двадцати восьми стран, входящих в Европейский союз, а игрок должен его угадать. \n\n\n") 
a = ['Австрия', 'Бельгия', 'Болгария', ' Великобритания', 'Венгрия','Германия','Греция','Дания','Ирландия','Испания','Италия','Кипр','Латвия','Литва','Люксембург','Мальта','Нидерланды','Польша','Словакия','Словения','Португалия','Румыния','Финляндия','Франция','Хорватия','Чехия','Швеция','Эстония',]
b = random.randint(0, 28)

answer = ''
while b != answer:
     answer = input ("Введите ваш вариант")
     if b == answer:
       print ("Молодец, возьми с полки пряник")
     else:
       print ("С кем не бывает")
	
	
input ("Нажмите Enter для выхода.")
