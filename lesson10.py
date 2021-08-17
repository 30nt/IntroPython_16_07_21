# модуль os
# работа с файлами

import os


def add_suffix_to_filename(filename, suffix):
    filename, ext = filename.rsplit(".", 1)
    filename = f"{filename}_{suffix}.{ext}"
    return filename


if __name__ == "__main__":
    path = "HW"
    filename = "lesson9.txt"
    path_filename = os.path.join(path, filename)
    print(path_filename)

# txt_file = open(path_filename, "r")
# data = txt_file.read()
# txt_file.close()

# with open(path_filename, "r") as txt_file:
#     data = []
#     for line in txt_file.readlines():
#         data.append(line.strip())
#
# data.append("TEST")
#
# new_filename = add_suffix_to_filename(filename, "copy")
# with open(os.path.join(path, new_filename), "w") as txt_file:
#     # txt_file.write("\n".join(data))
#     data = [f"{line}\n" for line in data]
#     txt_file.writelines(data)

# print(type(data))
# print(data)


# list_dir = os.listdir(path)
# print(list_dir)
# files = []
# for filename in list_dir:
#     path_filename = os.path.join(path, filename)
#     check_file = os.path.isfile(path_filename)   # f"{path}/{filename}" - не очень хорошо
#     if check_file:
#         files.append(filename)
# print(files)
#
# current_dir = os.getcwd()
# print(current_dir)


# EASY
# my_str = "abcdefg"
# result = []
#
# my_str = f"{my_str}_" if len(my_str) % 2 else my_str
# for index in range(0, len(my_str), 2):
#     result.append(my_str[index: index + 2])
################
# for index, value in enumerate(my_str):
#     if index % 2 == 0:
#         couple = my_str[index:index+2]
#         if len(couple)>1:
#             result.append(couple)
#         else:
#             result.append(value+"_")
# print("EASY", result)
