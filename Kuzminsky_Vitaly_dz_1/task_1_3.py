def transform_string(n: int):
    figures = [int(a) for a in str(n)] # разбиваем число на цифры
    if len(figures) == 1: # если длинна списка в 1 элемент, то:
        if figures[-1] == 1: # проверяем элемент и в зависимости от результата склоняем
            ending = 'процент'
        elif figures[-1] >= 2 and figures[-1] <= 4:
            ending = 'процента'
        else:
            ending = 'процентов'
    else:
        if figures[-2] == 1: # проверяем исключение, если предпоследний элемент списка = 1, то
            ending = 'процентов'
        else:
            if figures[-1] == 1: # проверяем последний элемент списка и в зависимости от результата склоняем
                ending = 'процент'
            elif figures[-1] >= 2 and figures[-1] <= 4:
                ending = 'процента'
            else:
                ending = 'процентов'
    return f'{n} {ending}' # склеиваем и возвращаем результат

for n in range(1, 101):
    print(transform_string(n))

print('end')