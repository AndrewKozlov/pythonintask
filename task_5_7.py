# Задача 5. Вариант 7. 
# Напишите программу, которая бы при запуске случайным образом отображала имя одного из семи гномов, друзей Белоснежки. 
# Videneev P. A. 
# 26.05.2016 

print("\nимя одного из семи гномов, друзей Белоснежки:") 

import random 
gnomes=["Doc","Bashful","Sneezy","Happy","Dopey","Sleepy","Grumpy"] 
p=random.choice(gnomes) 
print(p) 
input("Нажмите Enter для выхода")