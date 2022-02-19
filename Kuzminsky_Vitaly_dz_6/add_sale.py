import sys


def main(argv):
    """в CLI принимает значения продаж за день формата 1111,11 и записывает в файл bakery.csv"""
    program, revenue = argv
    revenue = revenue.replace(",", ".")
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        f.write(f'{revenue}\n')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        exit(main(sys.argv))
    else:
        print('Введите доход за день')
