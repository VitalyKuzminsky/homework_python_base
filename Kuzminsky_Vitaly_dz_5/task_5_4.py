def get_numbers(src: list):
    """Вывод элементов, значения которых больше предыдущего"""
    return [src[element] for element in range(1, len(src)) if src[element] > src[element - 1]]


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(*get_numbers(src))
