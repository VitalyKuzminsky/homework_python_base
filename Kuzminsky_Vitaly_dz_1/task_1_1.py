def convert_time(duration: int): # ф-ция конвертации времени из секунд
    time_list = [] # Создаём пустой список, куда сложим секунды, минуты, часы и дни
    time_sec = duration % 60 # расчитываем от аргумента остаток для секунд
    time_list.append(time_sec) # добавляем секуды в список
    if (duration - time_list[0]) == 0:
        out_time = f'{time_list[0]} сек'
    else:
        time_min = ((duration - time_list[0]) % 3600)//60 # расчитываем от аргумента остаток для минут, убрав секунды
        time_list.append(time_min) # добавляем минуты
        if (duration - (time_list[1] * 60) - time_list[0]) == 0:
            out_time = f'{time_list[1]} мин {time_list[0]} сек'
        else:
            time_hour = (duration - time_list[0] - time_list[1]) % 86400 // 3600 # расчитываем от аргумента остаток для часов, убрав секунды и минуты
            time_list.append(time_hour) # добавляем часы
            if (duration - (time_list[2] * 3600) - (time_list[1] * 60) - time_list[0]) == 0:
                out_time = f'{time_list[2]} час {time_list[1]} мин {time_list[0]} сек'
            else:
                time_day = (duration - time_list[0] - (time_list[1] * 60) - (time_list[2] * 3600)) // 86400 # расчитываем дни
                time_list.append(time_day) # добавляем дни
                out_time = f'{time_list[3]} дн {time_list[2]} час {time_list[1]} мин {time_list[0]} сек' # выводим в строку результат
    return out_time # возвращаем результат функции

duration = 400153
result = convert_time(duration)
print(result)

print('end')