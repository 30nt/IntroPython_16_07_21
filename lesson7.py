# списки, методы списков (append, extend, pop)
# max, min, sum, sort, sorted
# генераторы списков
# множества
# практическая работа

# my_list = ["Aaaaaaaaaaaaaaa", "Aaaaaa", "a", "A"]
# my_list = ["QWE", "asd", "123", "!@#"]
# my_list = [3, 4, 1, 2]
# second_list = [10, 20, 30]
# print(my_list) #   функция
# my_list.clear()  # метод
# print(my_list)

# my_list.append(5)
# print(my_list)
# last_value = my_list.pop()
# print(my_list, last_value)
#
# new_list = my_list.copy()
# new_list.extend(second_list)
# print(new_list, my_list)

# my_list.sort()  # меняет начальный список!!!
# print(my_list)
# some_list = sorted(my_list)  # не меняет начальный список!!!
# print(some_list)

# min_ = min(my_list)
# # print(min_)
# print(sorted(my_list))
# print(ord("!"))

# ord_list = []
# for ord_number in range(ord('a'), ord('z') + 1):
#     ord_list.append(ord_number)

# ord_list = [ord_number for ord_number in range(ord('a'), ord('z') + 1)]
# print(ord_list)
# chr_list = [chr(ord_number) for ord_number in range(ord('a'), ord('z') + 1)]
# print(chr_list)
# alphabet = "".join(chr_list)
# print(alphabet)

# numbers = [16, 9, -1, -100, 100, 25, -2]
#
# result = [number ** 0.5 for number in numbers if number > 0]
#
# print(result)

# set
# my_list = [1, 1, 1, 1, 1, 1, 1, 11, 11, 100]
# my_list = ["John", 34, "Cop", 34, 34]
# my_set = set("kasjhfkasvdsygfkjzvjhza<kugakhnlsdfjhialgbvajhsbgkjyfeczjhcbjshadfk")  # множество не сохраняет порядок
# print(my_set)

# my_set_1 = set("qqwwee123")
# my_set_2 = set("asdqwe")
# new_set_intersection = my_set_1.intersection(my_set_2)
# print(new_set_intersection)
#
# new_set_union = my_set_1.union(my_set_2)
# print(new_set_union)
#
# new_set_difference = my_set_2.difference(my_set_1)
# print(new_set_difference)

# my_string = "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqwwwwwwwweeertyuuu"
#
# for symbol in set(my_string):
#     if my_string.count(symbol) == 3:
#         print(symbol)

list_1 = [(1,2), (3,4)]
res = set(list_1)