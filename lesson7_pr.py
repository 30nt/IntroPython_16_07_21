"""
1) У вас есть переменная my_str, тип - str. И переменная my_symbol, тип - str.
Напечатать ЧИСЛО сколько раз my_symbol встречается в my_str.
Пример:  my_str="blablacar", my_symbol="bla".
Вывод на экран:
2
"""
my_str = "blablacarblablacar"
my_symbol = "bla"

# result_1 = my_str.count(my_symbol)
# print(result_1)

"""
2) У вас есть переменная my_str, тип - str. Напечатать ЧИСЛО сколько 
РАЗНЫХ символов встречается в my_str. 
Большая и маленькая буква считается как один символ. 
Пробелы, запятые и т.д. считаем тоже как символы.
Пример:  my_str="bla BLA car". 
Вывод на экран:
6
"""
my_str = "bla BLA car"
# my_str = my_str.lower()
# result_2 = len(set(my_str))
# print(result_2)
#
# symbol_bin = []
# for symbol in my_str:
#     if symbol not in symbol_bin:
#         symbol_bin.append(symbol)
# result_2 = len(symbol_bin)
# print(result_2)



"""
3)
Дана строка my_str и пустой список my_list.
Заполнить my_list символами из my_str, 
которые стоят на четных местах в строке (считаем с 0)
"""
# my_str = "qwerty"
# my_list = []
# print(id(my_list))
# my_list.extend(list(my_str[::2]))
# print(my_list)
# print(id(my_list))

"""
4)
Дана строка my_str, список str_index целых чисел в диапазоне от 
0 до длинны строки минус 1, пустой список my_list.
Заполнить my_list символами из my_str, которые стоят на местах с 
индексами из str_index
"""
# my_str = "qwerty"
# my_list = []
# str_index = [3, 2, 5, 5, 1, 0, 5, 0, 3, 2, 1]
# for index in str_index:
#     my_list.append(my_str[index])
# print(my_list)


"""
5)
Дано целое число (int). Определить сколько цифр в этом числе.
"""
my_number = 7812481234125126354123641275238541034182680000
# res_5 = len(str(my_number))
# print(res_5)

"""
6)
Дано целое число. Определить наибольшую цифру в этом числе.
"""
# res_6 = max(str(my_number))
# print(res_6)

"""
7)
Дано целое число. Составить число (int) с цифрами в обратном порядке.
"""

# my_number_str = str(my_number)
# new_number = my_number_str[::-1]
# new_number = int(new_number)
# new_number = int(str(my_number)[::-1])
# print(new_number)

"""
8)
Дано целое число. Составить число с цифрами в порядке возрастания(убывания).
"""

my_number_str = str(my_number)
sort_digits = sorted(my_number_str, reverse=True)
res_8 = int("".join(sort_digits))

print(res_8)