def thesaurus(*args) -> dict:
    """
    Функция, принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
    в котором ключи — первые буквы имён, а значения — списки, содержащие имена,
    начинающиеся с соответствующей буквы
    """
    dict_out = {}

    for elemet in args:
        if dict_out.get(elemet[0]) == None:
            dict_out.setdefault(elemet[0], [elemet])
        else:
            dict_out.get(elemet[0]).append(elemet)
    #dict_out = dict(sorted(dict_out.items()))

    return dict_out


print(thesaurus("Иван", "Мария", "Петр", "Илья"))
#print(thesaurus("Иван", "Мария", "Петр", "Илья", "Артем"))

print('and')