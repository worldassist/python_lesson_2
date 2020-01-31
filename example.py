#Задачи на циклы и оператор условия------
#----------------------------------------

'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
# i = 0
# while i < 5:
#     i += 1
#     print( i, 'is 0')

'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
# x = 0
# for i in range(10):
#     n = input('Напишите любую цифру: ')
#     if '5' in n:
#         x += 1
# print('Количество пятёрок равно', x)
'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
# sum = 0
#
# for i in range(1,101):
#     sum+=i
# print(sum)

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
# sum = 1
#
# for i in range(2, 11):
#     sum*=i
# print(sum)

'''
Задача 5
Вывести цифры числа на каждой строчке.
'''

# integer_number = 1617456
#
# #print(integer_number%10,integer_number//10)
#
# while integer_number>0:
#     print(integer_number%10)
#     integer_number = integer_number//10

'''
Задача 6
Найти сумму цифр числа.
'''
# integer_number = 5678
# sum = 0
# while integer_number>0:
#     sum += integer_number%10
#     integer_number = integer_number//10
# print('сумма цифр:', sum)

'''
Задача 7
Найти произведение цифр числа.
'''
# integer_number = 3289145
# z = 1
# while integer_number>0:
#     z *= integer_number%10
#     integer_number = integer_number//10
# print('произведение цифр числа:', z)

'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
# integer_number = 4672495
# while integer_number>0:
#     if integer_number%10 == 5:
#         print('Yes')
#         break
#     integer_number = integer_number//10
# else: print('No')

'''
Задача 9
Найти максимальную цифру в числе
'''
# integer_number = 13579
# q = 0
# while integer_number>0:
#     if integer_number%10 >= q:
#         q = integer_number%10
#     integer_number = integer_number//10
# print('максимальное число:', q)

'''
Задача 10
Найти количество цифр 5 в числе
'''
integer_number = 55545
p = 0
while integer_number>0:
    if integer_number%10 == 5:
        p += 1
    integer_number = integer_number//10
print('количество цифр 5 :', p)
