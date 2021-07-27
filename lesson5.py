from random import randint

# типы данных, приведение типов (str, int, float, bool), логические операторы
# обработка исключений
# условный оператор if, тернарный оператор
# цикл с условием (while)
# работа со строками

my_str = "-12345"
print(my_str.isupper())

# if условие:
#     блок если ДА
# elif условие2:
#     блок если ДА
# elif условие3:
#     блок если ДА
# ...........
# else:
#     блок если НЕТ

value = randint(10, 200)
if value < 100:
    print(f"Число {value} меньше 100")
else:
    print(f"Число {value} больше или равно 100")

#######################################################################
if not value % 3 and not value % 2:   # четное число, пример: 10 % 2 = 0
    print("Делится на 6")
elif not value % 3:
    print("Делится на 3")
elif value % 5 == 0:
    print("Делится на 5")
elif not value % 2:
    print("Делится на 2")

#######################################################
if not value % 2:
    result = value // 2
else:
    result = value // 2 + 1

# result = знач если да if условие else знач если нет
result = value // 2 if not value % 2 else value // 2 + 1

print(value, result)










# типы данных, приведение типов (str, int, float, bool), логические операторы
value = 10
value = str(value)
print(value, type(value))

value = input("Bool value")
result = value not in ("False", "0", "false")
# result = value * 2
print(result)

my_string = "kqhfkasjnvkoahfjamckkaugfjcbz c;sckgajcb zbjcyagjcn<"
print("o" in my_string)

# обработка исключений
value = input("Int value:")
try:
    result = 1 / int(value)
    print(result)
except ValueError:
    print("Это не целое число")
except ZeroDivisionError:
    print("На ноль делить нельзя!")