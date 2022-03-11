from warehouse_office_equipment.office_equipment import Printer, Copier, Scanner
from warehouse_office_equipment.werehouse import Warehouse
from warehouse_office_equipment.divisions import Divisions


printer_1 = Printer('Samsung', 'M2020')
print(printer_1.to_print(10))  # Принтер модель Samsung M2020 напечатал 10 страниц.
scaner_1 = Scanner('Canon', 'LiDE400')
print(scaner_1.to_scan(4800))  # Сканер Canon LiDE400 завершил работу с разрешением 4800 т/д.
copier_1 = Copier('Xerox', 'WorkCenter 5222')
print(copier_1.to_copy(50))  # Копир Xerox WorkCenter 5222 завершил одностороннее копирование 50 страниц.
print(copier_1.to_copy(100, True))  # Копир Xerox WorkCenter 5222 завершил двухстороннее копирование 100 страниц.
werehouse = Warehouse('Склад оргтехники')
print(werehouse.open())  # Склад оргтехники открыт.
print(werehouse.receipt_of_equipment(printer_1, 5))  # Оборудование Samsung M2020 добавлено на склад в количестве 5 шт.
print(werehouse.receipt_of_equipment(scaner_1, 3))  # Оборудование Canon LiDE400 добавлено на склад в количестве 3 шт.
print(werehouse.receipt_of_equipment(copier_1, 2))
# Оборудование Xerox WorkCenter 5222 добавлено на склад в количестве 2 шт.
print('-----------------------')
division_1 = Divisions('Бухгалтерия')
division_2 = Divisions('Отдел продаж')
print(werehouse.transfer_equipment(printer_1, 2, division_1))
# Оборудование Samsung M2020 в количестве 2 шт передано в подразделение Бухгалтерия 3 шт.
printer_2 = Printer('HP', 'P2055')
print(werehouse.receipt_of_equipment(printer_2, 50))  # Оборудование HP P2055 добавлено на склад в количестве 50 шт.
print(werehouse.transfer_equipment(printer_2, 30, division_2))
# Оборудование HP P2055 в количестве 30 шт передано в подразделение Отдел продаж 20 шт.
print(werehouse.remains(printer_1))  # На складе хранится 3 шт Samsung M2020.
print(werehouse.remains(printer_2))  # На складе хранится 20 шт HP P2055.
print(werehouse.transfer_equipment(copier_1, 5, division_2))
# Вы пытаетесь забрать со склада больше (5 шт), чем доступно: 2 шт.
print('-----------------------')
print(division_1.quantity(printer_1))  # За подразделением Бухгалтерия числится 2 шт Samsung M2020.
print(division_1.quantity(copier_1))  # Такого оборудования (Xerox WorkCenter 5222) в подразделении Бухгалтерия нет.
