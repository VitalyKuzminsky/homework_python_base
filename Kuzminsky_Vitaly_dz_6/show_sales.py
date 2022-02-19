import sys


def main(begin: int, end: int):
    """принимает два именновынных аргумента для отчёта по продажам <начало> и <конец> и выдаёт результат за период"""
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        data = f.readline()
        start_line = 1
        while (start_line <= end) or (end == 0 and data):
            if start_line >= begin:
                print(data.strip())
            data = f.readline()
            start_line += 1


if __name__ == '__main__':
    if len(sys.argv) == 1:
        exit(main(1, 0))
    elif len(sys.argv) == 2:
        program, begin = sys.argv
        exit(main(int(begin), 0))
    elif len(sys.argv) == 3:
        program, begin, end = sys.argv
        exit(main(int(begin), int(end)))
    else:
        print('Введите период продаж')
