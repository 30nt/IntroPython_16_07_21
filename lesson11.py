# json
import json

filename = "data.txt"
# data = ['1', '2', '3', "4", 5]

result = {"res": "test",
          "test": 100}
data = {"name": "John",
        "tuple": result}

# data_str = json.dumps(data)
# print(data_str, type(data_str))
# # data_str = "['1', '2']"
# new_data = json.loads(data_str)
# print(new_data, type(new_data))

with open("data.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

with open("data.json", "r") as json_file:
    new_data = json.load(json_file)

print(new_data)