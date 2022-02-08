from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count: int) -> list:
    """Возвращает список шуток в количестве count"""

    list_out = []
    for element in range(count):
        list_out.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')

    return list_out


def check_min_len(count: int) -> int:
    """Проверяет минимальную длину списков для формирования шуток"""

    if len(adverbs) > len(nouns) < len(adjectives):
        min_len = len(nouns)
    elif len(nouns) > len(adverbs) < len(adjectives):
        min_len = len(adverbs)
    else:
        min_len = len(adjectives)
    return min_len


def get_jokes_adv(count: int, possible: bool = True) -> list:
    """
    Возвращает список шуток в количестве count.
    Есть возможность устновить флаг, разрешающий или запрещающий повторы слов в шутках
    (когда каждое слово можно использовать только в одной шутке).

    :param count: int -- количетсво шуток
    :param possible: bool -- флаг. Default = True (без ограничений).
    :return: list шуток
    """

    list_out = []
    if possible == True:
        for element in range(count):
            list_out.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
    else:
        if count > check_min_len(count): #тут ф-ия вызываетс 2 раза, как-то тупо
            count = check_min_len(count)
            for element in range(count):
                list_out.append(f'{nouns.pop()} {adverbs.pop()} {adjectives.pop()}')
        else:
            for element in range(count):
                list_out.append(f'{nouns.pop()} {adverbs.pop()} {adjectives.pop()}')

    return list_out


print(get_jokes(2))
print(get_jokes_adv(10, False))

print('and')