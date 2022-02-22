import os

path_for_analysis = 'some_data'


def file_size_statistics(path: str):
    """Принимает путь папки для вывода статистики сколько файлов какого размера с шагом в 1 порядок,
    начиная до 100 байт"""
    keys_list_size = []
    for ways, folders, files in os.walk(path):
        if not files:
            return print(f'Файлов для анализа не найдено')
        keys_list_size.extend((os.path.getsize(os.path.join(ways, el)) for el in files))

    max_key = len(list(str(max(keys_list_size))))
    file_size = [10 ** degree for degree in range(2, max_key + 1)]  # для изменения размера выдачи можно 2 заменить на 1

    dict_size = {}
    for key in keys_list_size:
        for size in file_size:
            if key < size:
                dict_size.update({size: dict_size.get(size, 0) + 1})
                break

    return dict(sorted(dict_size.items()))


print(file_size_statistics(path_for_analysis))
