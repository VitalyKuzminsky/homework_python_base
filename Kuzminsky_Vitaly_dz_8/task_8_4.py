from functools import wraps


def args_func(*args):
    if len(args) != 1:
        raise ValueError(f'wrong value: {args}')
    if not isinstance(args[0], int) or args[0] <= 0:
        raise ValueError(f'wrong value: {args[0]}')


def val_checker(func):
    def _val_checker(main_func):
        @wraps(main_func)
        def wrapper(*args):
            func(*args)
            return main_func(*args)
        return wrapper
    return _val_checker


@val_checker(args_func)  # не забудьте про аргумент-функцию
def calc_cube(x):
    """Возведение числа в третью степень"""
    return x ** 3


if __name__ == '__main__':
    print(calc_cube(5))
    print(calc_cube('ss'))
