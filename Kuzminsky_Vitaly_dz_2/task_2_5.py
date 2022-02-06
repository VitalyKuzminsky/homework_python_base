from random import uniform

def transfer_list_in_str(list_in: list) -> str:
    """Преобразует каждый элемент списка (вещественное число) в строку вида '<r> руб <kk> коп' и
            формирует из них единую строковую переменную разделяя значения запятой."""
    i = 0
    new_list = []
    while i < len(my_list):
        rub = int(my_list[i] // 1)
        kop = int((my_list[i] - rub) * 100) # !!! проблема с округлением, не знаю как решить???
        new_list.append(f'{rub} руб {kop:02d} коп')
        i += 1
    str_out = ', '.join(new_list)
    return str_out

my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]
print(f'Исходный список: {my_list}')
result_1 = transfer_list_in_str(my_list)
print(result_1)
print()

def sort_prices(list_in: list) -> list:
    """Сортирует вещественные числа по возрастанию, не создавая нового списка"""
    list_in.sort()
    return list_in


print(f'Исходный список по id: {id(my_list)} {my_list}')
result_2 = sort_prices(my_list)
print(f'Док-во, что result_2 остался тем же объектом в id: {id(result_2)}')
print(result_2)
print()


def sort_price_adv(list_in: list) -> list:
    """Создаёт новый список и возвращает список с элементами по убыванию"""
    list_out = sorted(list_in, reverse=True)
    return list_out


result_3 = sort_price_adv(my_list)
print(result_3)
print()


def check_five_max_elements(list_in: list) -> list:
    """Проверяет элементы входного списка вещественных чисел и возвращает
        список из ПЯТИ максимальных значений"""
    list_out = result_3[:5:]
    return list_out


result_4 = check_five_max_elements(my_list)
print(result_4)



print('end')