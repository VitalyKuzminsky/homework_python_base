from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args):
        print(f"{func.__name__}({', '.join(f'{str(el)}: {type(el)}' for el in args)})")
        return func(*args)
    return wrapper


@type_logger
def calc_cube(x):
    """Возведение числа в третью степень"""
    return x ** 3


a = calc_cube(5)
print(a)
a = calc_cube(5, 55, 555)
print(a)
