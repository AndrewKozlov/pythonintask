# Задача 4. Вариант 22. 
# Напишите программу, которая выводит имя, под которым скрывается Самюэл Ленгхорн Клеменс. Дополнительно необходимо вывести область интересов указанной личности, место рождения, годы рождения и смерти (если человек умер), вычислить возраст на данный момент (или момент смерти). Для хранения всех необходимых данных требуется использовать переменные. После вывода информации программа должна дожидаться пока пользователь нажмет Enter для выхода.
# Nikishin P. S. 
# 12.05.2016


name = "Самюэл Ленгхорн Клеменс"
mestoro = "Флорида, Миссури, США)"
dataro = int(1835)
datasm = int(1910)
years = int(datasm - dataro)
interesi = "Литература"
 
print(name+" более известен как писатель Марк Твен")
print("Место рождения: "+mestoro)
print("Год рождения: "+str(dataro))
print("Год смерти: "+str(datasm))
print("Возраст: "+str(years))
print("Область интересов: "+interesi)

input("\nДля выхода нажмите Enter") 
