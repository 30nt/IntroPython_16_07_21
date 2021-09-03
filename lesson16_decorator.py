from time import time

def time_decorator(some_func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = some_func(*args, **kwargs)
        print("Time of func:", time() - start_time)
        return result
    return wrapper


@time_decorator
def product_numbers(number):
    product = 1
    for numb in range(1, number + 1):
        product *= numb
    return product

# new_product_numbers = time_decorator(product_numbers)
# result = new_product_numbers(100000)


# start_time = time()
result= product_numbers(100000)
# print(time() - start_time)