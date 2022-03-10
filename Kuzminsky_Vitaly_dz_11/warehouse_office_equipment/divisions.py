class Divisions:
    def __init__(self, name):
        self.name = name
        self.division_equipment = dict()

    def description(self):
        """Наименование подразделения"""
        return f'{self.name}'

    def trans_to_division(self, name, count):
        """Поступление техники со склада в подразделение"""
        self.division_equipment.setdefault(name, count)

    def quantity(self, name):
        """Проверка количества оборудования в подразделении"""
        if self.division_equipment.get(name) == None:
            return f'Такого оборудования ({name.introduce_yourself()}) в подразделении {self.description()} нет.'
        return f'За подразделением {self.description()} числится' \
               f' {self.division_equipment.get(name)} шт {name.introduce_yourself()}.'
