# Задача 6. Вариант 22.
# Создайте игру, в которой компьютер загадывает имена двух братьев, легендарных
# основателей Рима, а игрок должен его угадать.

# Щербаков Р.А.
# 22.05.2016

import random

print("Комп загадал имя одного из двух братьев основавшие рим, попробуй угадать что ли")
name='Рем', 'Ромул'
rand=random.randint(0,1)
ugad=""
while ugad!=name[rand]:
    ugad=input("Введите слово:") 
	
input("Вы наконец то угадали!\n\nok")
