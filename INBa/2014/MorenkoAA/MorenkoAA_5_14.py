﻿# Задача 5, Вариант 14 
# Напишите программу, которая бы при запуске случайным образом отображала название одной из двадцати башен Московского кремля.

# Моренко А.А.
# 16.03.2016

import random
print('Программа случайным образом отображает название одной из двадцати названий башен Кремля')
feat = random.randint(1,20)
print('Одна из башен называется:', end=" ")
if feat == 1 :
    print("Беклемишевская башня")
elif feat == 2 :
    print("Беклемишевская башня")
elif feat == 3 :
    print("Набатная башня")
elif feat == 4 :
    print("Царская башня")
elif feat == 5 :
    print("Спасская башня")
elif feat == 6 :
    print("Сенатская башня")
elif feat == 7 :
    print("Никольская башня")
elif feat == 8 :
    print("Угловая Арсенальная башня")
elif feat == 9 :
    print("Средняя Арсенальная башня")
elif feat == 10 :
    print("Троицкая башня")
elif feat == 11 :
    print("Кутафья башня")
elif feat == 12 :
    print("Комендантская башня")
elif feat == 13 :
    print("Оружейная башня")
elif feat == 14 :
    print("Боровицкая башня")
elif feat == 15 :
    print("Водовзводная башня")
elif feat == 16 :
    print("Благовещенская башня")
elif feat == 17 :
    print("Тайницкая башня")
elif feat == 18 :
    print("Первая Безымянная башня")
elif feat == 19 :
    print("Вторая Безымянная башня")
else:
    print("Петровская башня")
input ('Нажмите Enter для выхода')