def convert_list_in_str(list_in: list) -> str:
    """Обособляет каждое целое число кавычками, добавляя кавычку до и после элемента
        списка, являющегося числом, и дополняет нулём до двух целочисленных разрядов.
        Формирует из списка результирующую строковую переменную и возвращает."""

    i = 0
    new_list_in = []
    while i < len(list_in):
       for element in list_in:
           if element.isnumeric():
               element = f'"{int(element):02d}"'
           elif element[0] == '+':
               element = f'"+{int(element):02}"'
           new_list_in.append(element)
           i += 1
    str_out = ' '.join(new_list_in)
    return str_out


my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = convert_list_in_str(my_list)
print(result)



print('end')