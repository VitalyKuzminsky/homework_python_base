def convert_name_extract(list_in: list) -> list:
    """Извлекает имена из элементов и формирует список приветствий."""
    i = 0
    list_out = []
    while i < len(list_in): # ничего умнее не пришло в голову, чем перебрать список. Уверен, есть простое решение =)
        list_elemet_revers = list(reversed(list_in[i]))  #реверснуть каждый элемент
        new_str_element = ''.join(list_elemet_revers) #собрать обратно в строку
        name_revers = new_str_element[:new_str_element.index(' '):] #получаем имя, выбрав срез до пробела
        name = name_revers[::-1] #реверс, чтобы имя стало нормальным
        list_out.append(f'Привет, {name.capitalize()}!') #собираем список, форматируя
        i += 1
    return list_out


my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
result = convert_name_extract(my_list)
print(result)

print('end')