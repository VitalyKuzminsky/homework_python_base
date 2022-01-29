def sum_list_1(my_list: list): # ф-ия, где аргумент список найденных кубов
    indx = 0
    list_divisible_7 = []
    while indx < len(my_list): # перебираем все элементы списка чисел
        num = my_list[indx]
        figures = [int(a) for a in str(num)] # создём из каждого элемента новый список из цифр
        if sum(figures) % 7 != 0: # проверяем делится ли сумма цифр на 7: не делится - пропускаем, делится добавляем в новый список
            indx += 1
            continue
        list_divisible_7.append(my_list[indx])
        indx += 1
    return sum(list_divisible_7) # Вычисляем сумму чисел списка, сумма цифр которых делится нацело на 7. Возвращаем результат

def sum_list_2(my_list: list): # ф-ия, где аргумент список найденных кубов, но создаём новый список, к каждому элементу добавляем 17 и повторяем код ф-ии sum_list_1
    new_my_list = []
    i = 0
    while i < len(my_list):
        new_my_list.append(my_list[i] + 17)
        i += 1

    indx = 0
    list_divisible_7 = []
    while indx < len(new_my_list): # перебираем все элементы списка чисел,
        num = new_my_list[indx]
        figures = [int(a) for a in str(num)] # создём из каждого элемента новый список из цифр
        if sum(figures) % 7 != 0: # проверяем делится ли сумма цифр на 7: не делится - пропускаем, делится добавляем в новый список
            indx += 1
            continue
        list_divisible_7.append(new_my_list[indx])
        indx += 1
    return sum(list_divisible_7) # Вычисляем сумму чисел списка, сумма цифр которых делится нацело на 7. Возвращаем результат

number = 0
my_list = []
# создаём список нечетных чисел от 0 до 1000, возведённых в куб
while number <= 1000:
    if number % 2 == 0:
        number += 1
        continue
    my_list.append(number ** 3)
    number += 1

result_1 = sum_list_1(my_list)
print(result_1)
result_2 = sum_list_2(my_list)
print(result_2)

print('end')










