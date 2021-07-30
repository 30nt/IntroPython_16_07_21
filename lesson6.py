# цикл с условием (while)
# строки, форматирование строк, срезы
# цикл for
# кортежи, списки, копии списков

# кортежи, списки, копии списков

value = [123]
my_tuple = (value, 1, 2, 3, "qwe", True, ("a", "z"), [True])  # итерируемый объект, не изменяемый объект
my_list = [1, 2, 3, "qwe", False]  # итерируемый объект, изменяемый объект
list_ = [1, 2, 3]
# my_tuple[-2][0] = 100
print(my_tuple)
new_list = list(my_tuple)
new_list[0] = "qweqweqwe"
my_tuple = tuple(new_list)
print(my_tuple)



# new_list = my_list.copy()
new_list = my_list[:]

new_list[0] = 100
print(new_list, my_list)

my_list = [0]
new_list = [my_list] * 3
my_list[0] = 100
print(new_list)


print(type(my_tuple), my_tuple)
print(type(my_list), my_list)

print(my_list[-1])
for value in my_tuple:
    print(value)

new_tuple = my_tuple[::-1]
print(new_tuple)

my_list[-1] = 11
print(my_list)

# my_tuple[0] = 11  # TypeError
# print(my_tuple)








# цикл for
my_str = "qwErtYasdfgh87216^%$^&^("  # итерация, итерируемый объект
for symbol in my_str:
    if symbol.isupper():
        print(symbol)
for symbol in my_str:
    if symbol.isalpha() and symbol.lower() not in "eyuioa":
        print(symbol)


# строки, форматирование строк, срезы

my_str = "qwertyt"
print(id(my_str))
my_str = "qwerty"
print(id(my_str))
print(my_str)

print(my_str[3])
print(my_str[-1])
# print(my_str[-10]) #IndexError

print(my_str[1:-1])  # werty
print(my_str[1:2])
print(my_str[1:])
print(my_str[10:-100])
new_str = my_str[:-1]
print(id(new_str))

my_str = "0123456789"
print(my_str[::2]) # четные индексы
print(my_str[1::2]) # нечетные индексы
print(my_str[-4:0:-1])
new_str = my_str[:7]
new_str = new_str[::-1]
print(new_str)


# цикл с условием (while)
# while условие:
#     блок действий

# while True:
#     print("Бесконечный цикл")
#     break

# count = 0
# while count < 100:
#     print("цикл:", count)
#     count += 1  # ------> count = count + 1

value = input("Введите символ:")
while value.isalpha():  # если буква, то печатаем, если другой символ - выходим
    print(f"Letter: {value}")
    value = input("Введите символ:")

# do_input_value = True
# while do_input_value:
#     value = input("Введите символ:")
#     if value.isalpha():
#         print(f"Letter: {value}")
#     else:
#         do_input_value = False
