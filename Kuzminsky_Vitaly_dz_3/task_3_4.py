def thesaurus_adv(*args) -> dict:
    """
    Функция. принимающую в качестве аргументов строки в формате «Имя Фамилия» и
    возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари
    """
    dict_in = {}
    for elemet in args:
        if dict_in.get(elemet[elemet.index(' ')+1]) == None:
            dict_in.setdefault(elemet[elemet.index(' ')+1], [elemet])
        else:
            dict_in.get(elemet[elemet.index(' ')+1]).append(elemet)

    dict_out = dict(sorted(dict_in.items())) # туплю, не могу понять, как мне перебрать значения словаря, сделав из них словарь по именам
    return dict_out


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))

print('and')