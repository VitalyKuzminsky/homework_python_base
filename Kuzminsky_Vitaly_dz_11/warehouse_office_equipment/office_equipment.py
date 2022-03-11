class OfficeEquipment:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def introduce_yourself(self):
        """Описание оборудования"""
        return f'{self.brand} {self.model}'


class Printer(OfficeEquipment):
    def __init__(self, brand, model):
        super().__init__(brand, model)

    def to_print(self, number):
        """Запустить печать на принтере"""
        return f'Принтер {self.introduce_yourself()} напечатал {int(number)} страниц.'


class Scanner(OfficeEquipment):
    def __init__(self, brand, model):
        super().__init__(brand, model)

    def to_scan(self, permission):
        """Отсканировать"""
        return f'Сканер {self.introduce_yourself()} завершил работу с разрешением {permission} т/д.'


class Copier(OfficeEquipment):
    def __init__(self, brand, model):
        super().__init__(brand, model)

    def to_copy(self, number, double_sided=False):
        """Снять копии. По умолчанию одностороннее копирование."""
        if double_sided:
            return f'Копир {self.introduce_yourself()} завершил двухстороннее копирование {number} страниц.'
        return f'Копир {self.introduce_yourself()} завершил одностороннее копирование {number} страниц.'
