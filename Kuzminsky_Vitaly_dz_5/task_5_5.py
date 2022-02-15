def get_uniq_numbers(src: list):  # O(n**2)
    """ Определяет элементы списка, не имеющие повторений.
    Формирует из этих элементов список с сохранением порядка их следования в исходном списке"""
    return [element for element in src if src.count(element) == 1]


def get_uniq_numbers_adv(src: list):  # O(n)
    """ Определяет элементы списка, не имеющие повторений.
        Формирует из этих элементов список с сохранением порядка их следования в исходном списке"""
    unique_numbers = set()
    temp = set()
    for element in src:
        if element not in temp:
            unique_numbers.add(element)
        else:
            unique_numbers.discard(element)
        temp.add(element)
    return [element for element in src if element in unique_numbers]


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(*get_uniq_numbers(src), type(get_uniq_numbers(src)))
print(*get_uniq_numbers_adv(src), type(get_uniq_numbers_adv(src)))
