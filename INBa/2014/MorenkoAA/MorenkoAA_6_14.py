﻿# Задача 6, Вариант 12 
# Создайте игру, в которой компьютер загадывает имя одного из трех официальных талисманов зимних Олимпийских игр 2014 года в Сочи, а игрок должен его угадать.

# Моренко А.А.
# 3.04.2016

import random
tals = random.randrange(3)
tal = ("Леопард","Белый мишка","Зайка")
print ('Отгадайте название одного из талисманов зимних олимпийских игр в Сочи 2014 года!')
user_tal = input ('Введите Ваш вариант: ')
while user_tal.lower() != tal[tals].lower():
user_tal = input ('Вы не угадали,попробуйте ещё раз: ')
print ('Вы угадали!')
input ('Нажмите Enter для выхода')