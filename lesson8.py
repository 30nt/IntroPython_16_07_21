# словари dict, методы словарей

# my_data = {"name": "John",
#            "age": 23,
#            "hobbies": ["dancing", "reading"]
#            }
#
# print(my_data["name"], my_data["hobbies"])
# my_data["surname"] = "Snow"
# my_data["age"] = 34
# my_data["age"] = 46
# print(my_data)

# ключи - любые НЕИЗМЕНЯЕМЫЕ объекты, значения - любые объекты
# my_dict = {"1": 1, 1: "1", "2": 22, (1, 2, "3"): "TEST", }
# print(my_dict)
# import random
#
# my_list = [1, 3, 6, 8]
# value = random.randint(1, 1000)
# if value % 3 == 1:
#     res = min(my_list)
# elif value % 3 == 2:
#     res = max(my_list)
# else:
#     res = sum(my_list)

# func_dict = {0: sum,
#              1: min,
#              2: max}
# res = func_dict[value % 3](my_list)
# print(value, res)

# value = my_dict.get("1")
# print(value)

# print("2" in my_dict)  # in смотрит в ключи
# key = 22
# if key in my_dict:
#     value = my_dict[key]
#     print(value)

# for key in my_dict: # for перебирает ключи
#     print(key, my_dict[key])

# print(list(my_dict.keys()))
# print(list(my_dict.values()))
# print(list(my_dict.items()))
#
# for key, value in my_dict.items():
#     print(key, value)

# my_dict_1 = {1: 11, 2: 22, 3: 33}
# my_dict_2 = {1: 111, 2: 222, 4: 444}

# new_dict = {}
# new_dict.update(my_dict_2)
# new_dict.update(my_dict_1)

# new_dict = {**my_dict_1, **my_dict_2}
# print(new_dict)

# address = {"city": "Dnipro",
#            "ZIP": 49000}
#
#
# person = {"name": "John",
#            "age": 23,
#            "hobbies": ["dancing", "reading"],
#           "address": address
#            }
#
# print(person["address"]["ZIP"])
import time

start_time = time.time()
price_list = [{"product": "MacBook", "price": 32000, "brand": "Apple"},
              {"product": "MacBookPro", "price": 52000, "brand": "Apple"},
              {"product": "HP", "price": 15000, "brand": "HP"}]

prices = []
for device in price_list:
    prices.append(device["price"])
max_price = max(prices)

for device in price_list:
    if device["price"] == max_price:
        print(device["product"])
print(f"time: {time.time() - start_time} sec.")

# value = 1, 2, 3, 4, "qwerty", [111, 222]
# print(value)

# распаковка кортежей (списков)
# value = (1, 2, 3)
# value = "qwe"
# val_1, val_2, val_3 = value
# print(val_3)

# number_1 = 5
# number_2 = 10
# number_2, number_1 = number_1, number_2
# tmp = number_1
# number_1 = number_2
# number_2 = tmp
# print(number_1, number_2)

# response = (200, "06.08.2021 19:29", "TimeZone: +2", "error_message: ValueError", 123,"ysdgfasyg", [])
# date_time, *_ = response
# print(date_time)

# image_shape = (800, 600, 3)
# w, h = image_shape[:2]

# print(*image_shape)