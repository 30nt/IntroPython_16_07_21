persons = [{"name": "John", "age": 15},
           {"name": "JohnSilver", "age": 15},
           {"name": "Jack", "age": 45},
           {"name": "JackDaniels", "age": 95}]

# ages = [person["age"] for person in persons]
# len_names = [len(person["name"]) for person in persons]
# min_age = min(ages)
# max_len_name = max(len_names)

ages = []
len_names = []
for person in persons:
    ages.append(person["age"])
    len_names.append(len(person["name"]))
min_age = min(ages)
max_len_name = max(len_names)

for person in persons:
    if person["age"] == min_age:
        print(person["name"])
print('-----------------------')
for person in persons:
    if len(person["name"]) == max_len_name:
        print(person["name"])

mean_age = sum(ages) / len(ages)
print(mean_age)

dict_1 = {1: 1, 2: 2}
dict_2 = {11: 11, 2: 22}

result_dict = dict_1.copy()
for key in dict_2:
    if key not in result_dict:
        result_dict[key] = dict_2[key]
    else:
        result_dict[key] = [dict_1[key], dict_2[key]]
print(result_dict)