#employee_list = ["John Snow", "Piter Pen", 
 #                "Drakula", "IvanIV", "Moana", "Juilet"]
#print(employee_list[1] + ","+ employee_list [-2])

#def dev_by_three(number):
#    if  number % 3 == 0 :
 #    return "ДА"
  #  else:
   #  print("Нет")

#num = 1
#result = dev_by_three (num)
#print(f"Делится ли на три {num}? - {result}")

#Напишите функцию min_boxes, которая принимает одно число — количество предметов — 
# и возвращает минимальное количество коробок, 
# необходимых для упаковки этих предметов, 
# если в одну коробку помещается не более пяти предметов.

#import math
#def min_boxes(items):
 #return math.ceil(items / 5)
#num_items = int(input ("Введите количество предметов: "))
#print(f"Минимальное количество коробок: {min_boxes(num_items)}")

#Напишите функцию check_divisibility, которая принимает одно число — n— и выводит все числа от 1 до n(включительно):
# Если число делится на 2, но не на 4, оно выводится с текстом «Делится на 2, но не на 4».
# Если число делится и на 2, и на 4, оно выводится с текстом «Делится и на 2, и на 4».
#Все остальные числа выводятся просто как есть.

#n= int(input ("Введите число: "))

#def check_divisibility(n):
    #for i in range (1, n + 1):
     #if i % 4 == 0 :
      # print (f"{i} - Делится и на 2, и на 4")
     #elif i % 2 == 0:  
      #print (f"{i} - Делится на 2, но не на 4")   
    # else:
       #print (i)

#check_divisibility(n)

#Напишите функцию quarter_of_year(), которая принимает один аргумент — номер месяца (от 1 до 12) — и возвращает номер квартала, к которому относится этот месяц.
#Например, если передать 5, на выходе должно быть II квартал, так как май относится ко второму кварталу.


#def quarter_of_year(month):
 #   if 1<= month<=3:
  #   return "1 квартал"
   # if 4<= month<=6:
    # return "2 квартал"
    #if 7<= month<=9:
    # return "3 квартал"
    #if 10<= month<=12:
    # return "4 квартал"
    #return "Неверный номер месяца"

#month = int(input ("Введите номер месяца (1-12): "))
#print(quarter_of_year(month))


#Необходимо вывести элементы, которые одновременно:больше 15,
#делятся на 3 без остатка.

#lst = [17, 34, 9, 21, 13, 48, 24, 7, 81, 29, 16, 12, 42]
#result = [x for x in lst if x > 15 and x % 3 ==0]
#print(result)

#Создайте список [25, 20, 15, 10, 5]с помощью функции range()
# и выведите его на экран.

#1 вариант КР
# for i in range (25, 0, -5):
    #print(i, end=' ')
#
# 2 вариант SP
# my_list = list(range(25, 0, -5))
#print(my_list)

#код, который меняет значение переменных местами
var_1 = 50
var_2 = 5

temp = var_1
var_1 = var_2
var_2 = temp

print("var_1 =", var_1)
print("var_2 =", var_2)