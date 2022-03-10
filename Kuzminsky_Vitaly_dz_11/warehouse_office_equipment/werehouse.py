from .divisions import Divisions


class Warehouse:
    def __init__(self, name):
        self.name = name
        self.our_equipment = dict()

    def open(self):
        """TODO"""
        return f'{self.name} открыт.'

    def receipt_of_equipment(self, name, count):
        """Поступление техники на склад"""
        if not isinstance(count, int):
            print(f'Нужно числовое значение оборудования!')
        else:
            self.our_equipment.setdefault(name, count)
            return f'Оборудование {name.introduce_yourself()} добавлено на склад в количестве {count} шт.'

    def transfer_equipment(self, name, count, division):
        """Передача техники со склада в подразделение"""
        if not isinstance(count, int):
            print(f'Нужно числовое значение оборудования!')
        else:
            if count > self.our_equipment.get(name):
                return f'Вы пытаетесь забрать со склада больше ({count} шт), ' \
                       f'чем доступно: {self.our_equipment.get(name)} шт.'
            self.our_equipment[name] = self.our_equipment.get(name) - count
            division.trans_to_division(name, count)  # добавляем в словарь подразделения
            return f'Оборудование {name.introduce_yourself()} в количестве {count} шт ' \
                   f'передано в подразделение {Divisions.description(division)}.'

    def remains(self, name):
        """Остатки техники на складе"""
        if self.our_equipment.get(name) == 0:
            return f'Оборудование {name.introduce_yourself()} на складе закончилось.'
        return f'На складе хранится {self.our_equipment.get(name)} шт {name.introduce_yourself()}.'
