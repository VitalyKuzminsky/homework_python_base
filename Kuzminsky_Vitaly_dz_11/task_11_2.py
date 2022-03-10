class MyError:
    def __init__(self, divisible, divider):
        try:
            res = divisible / divider
        except ZeroDivisionError:
            print('Нельзя делить на ноль')
        else:
            print(f'Всё хорошо. Результат деления равен: {res}')
        finally:
            print('Проверка завершена')


number_1 = int(input('Введите число:\n'))
number_2 = int(input('Введите число:\n'))
result = MyError(number_1, number_2)
