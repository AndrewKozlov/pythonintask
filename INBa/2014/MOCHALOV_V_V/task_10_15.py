﻿# -*- coding: UTF-8 -*-
# Задача 10. Вариант 15.
#
# Напишите программу "Генератор персонажей" для игры. Пользователю должно быть предоставлено 30 пунктов, которые можно распределить между четырьмя характеристиками: Сила, Здоровье, Мудрость и Ловкость. Надо сделать так, чтобы пользователь мог не только брать эти пункты из общего "пула", но и возвращать их туда из характеристик, которым он решил присвоить другие значения.
# Mochalov V. V.
# 14.05.2016

points=30
sila=0
zdr=0
mudr=0
lovk=0
k=0
while k<1:
 print("Вы имеете ", points," поинтов. Сила=", sila," Ловкость=", lovk," Мудрость=", mudr," Здоровье=", zdr) 
 print("Напишите куда вы хотите их потратить (Мудрость, Ловкость, Сила, Здоровье).")
 a=input("Для завершения редактирования напишите Хватит. ")
 if a=="Мудрость":
     q=input("Вы редактируете Мудрость. Прибавить или Отбавить очки?")
     if q=="Отбавить":
         q=input("Сколько очков отбавить?")
         if (mudr-int(q))>=0:
          mudr=mudr-int(q)
          points=points+int(q)
         else:
          print("Мудрость не может быть отрицательной.")
     elif q=="Прибавить":
         q=input("Сколько очков прибавить?")
         if (points-int(q))>=0:
          mudr=mudr+int(q)
          points=points-int(q)
         else:
          print("Недостаточно очков.")
 elif a=="Сила":
     q=input("Вы редактируете Силу. Прибавить или Отбавить очки?")
     if q=="Отбавить":
         q=input("Сколько очков отбавить?")
         if (sila-int(q))>=0:
          sila=sila-int(q)
          points=points+int(q)
         else:
          print("Сила не может быть отрицательной.")
     elif q=="Прибавить":
         q=input("Сколько очков прибавить?")
         if (points-int(q))>=0:
          sila=sila+int(q)
          points=points-int(q)
         else:
          print("Недостаточно очков.")
 elif a=="Ловкость":
     q=input("Вы редактируете Ловкость. Прибавить или Отбавить очки?")
     if q=="Отбавить":
         q=input("Сколько очков отбавить?")
         if (lovk-int(q))>=0:
          lovk=lovk-int(q)
          points=points+int(q)
         else:
          print("Ловкость не может быть отрицательной.")
     elif q=="Прибавить":
         q=input("Сколько очков прибавить?")
         if (points-int(q))>=0:
          lovk=lovk+int(q)
          points=points-int(q)
         else:
          print("Недостаточно очков.")
 elif a=="Здоровье":
     q=input("Вы редактируете Здоровье. Прибавить или Отбавить очки?")
     if q=="Отбавить":
         q=input("Сколько очков отбавить?")
         if (zdr-int(q))>=0:
          zdr=zdr-int(q)
          points=points+int(q)
         else:
          print("Здоровье не может быть отрицательным.")
     elif q=="Прибавить":
         q=input("Сколько очков прибавить?")
         if (points-int(q))>=0:
          zdr=zdr+int(q)
          points=points-int(q)
         else:
          print("Недостаточно очков.")
 elif a=="Хватит":
     k=99999
print("Редактирование персонажа завершено. Сила=", sila," Ловкость=", lovk," Мудрость=", mudr," Здоровье=", zdr) 
input("Для выхода нажмите Enter.")
