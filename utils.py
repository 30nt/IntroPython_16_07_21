from random import randint

L_LIMIT = -10
R_LIMIT = 10


def create_triangle(name="ABC", l_limit=L_LIMIT, r_limit=R_LIMIT):
    triangle = {key: {"x": randint(l_limit, r_limit), "y": randint(l_limit, r_limit)} for key in name}
    return triangle


def create_triangle_list(len_list):
    triangle_list = [create_triangle() for _ in range(len_list)]
    return triangle_list


# def create_triangle(name, l_limit=-100, r_limit=100):
#     key_a, key_b, key_c = name
#     triangle = {key_a: {"x": randint(l_limit, r_limit), "y": randint(l_limit, r_limit)},
#                 key_b: {"x": randint(l_limit, r_limit), "y": randint(l_limit, r_limit)},
#                 key_c: {"x": randint(l_limit, r_limit), "y": randint(l_limit, r_limit)}}
#     return triangle

print(__name__)

if __name__ == "__main__":
    tr = create_triangle()
    print(f"tr: {tr}")
