import re


def email_parse(email: str) -> dict:
    """
    Парсит переданную email-строку на атрибуты и возвращает словарь
    :param email: строковое входное значение обрабатываемого email
    :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
    """

    RE_MAIL = re.compile(r'(?P<key>([A-Za-z0-9]+[._-])*[A-Za-z0-9]+)@(?P<value>[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+)')
    mail_ok = RE_MAIL.match(email)
    if not mail_ok:
        raise ValueError(f'wrong email: {email}')
    return mail_ok.groupdict()


if __name__ == '__main__':
    email_parse('someone@geekbrains.ru')
    print(email_parse('someone@geekbrains.ru'))
    email_parse('someone@geekbrainsru')
    print(email_parse('someone@geekbrainsru'))


""" Второй вариант решения задачки"""

#    MAIL_OK = re.compile(r'([A-Za-z0-9]+[._-])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
#    RE_MAIL = re.compile(r'(?P<key>[^&!#$%~=,\'{}|]+)@(?P<value>[^&!#$%~=,\'{}|]+)')
#
#    if not re.fullmatch(MAIL_OK, email):
#        raise ValueError(f'wrong email: {email}')
#    else:
#        print(*map(lambda x: x.groupdict(), RE_MAIL.finditer(email)), sep=', ')
#
#
# if __name__ == '__main__':
#    email_parse('someone@geekbrains.ru')
#    email_parse('someone@geekbrainsru')
