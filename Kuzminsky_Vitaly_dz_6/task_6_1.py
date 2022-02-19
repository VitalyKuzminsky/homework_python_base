from pprint import pprint


def get_parse_attrs(line: str) -> tuple:
    """Парсит строку на атрибуты и возвращает кортеж атрибутов (<remote_addr>, <request_type>, <requested_resource>)"""

    data_line = line.split()
    return data_line[0], data_line[5].replace('"', ''), data_line[6]


list_out = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    for line in fr:
        list_out.append(get_parse_attrs(line))
    # передавайте данные в функцию и наполняйте список list_out кортежами

pprint(list_out)
