from utils import create_triangle, create_triangle_list


def print_list(some_list):
    for line in some_list:
        print(line)


print(__name__)

l_limit = -10
r_limit = 10
name2 = "ABC"
triangle_0 = create_triangle("XYZ")
print(triangle_0)
# triangle_2 = create_triangle(l_limit=-10, name="ABC", r_limit=10)  # именованная передача параметров
triangle_2 = create_triangle(l_limit=l_limit, name=name2, r_limit=r_limit)  # именованная передача параметров
triangle_list = create_triangle_list(5)
triangle_list_2 = [create_triangle(name2, l_limit, r_limit), create_triangle("VGY", r_limit=1, l_limit=-1)]
print_list(triangle_list)
print("--------------------")
print_list(triangle_list_2)
