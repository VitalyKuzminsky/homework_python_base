import datetime
import re


class Data:
    """
    Класс Data

    Требуется:
    import datetime
    import re
    """
    def __init__(self, date_in):
        self.date_in = date_in

    @classmethod
    def extracting_number(cls, date_in):
        RE_DATE = re.compile(r'(?P<day>([0-9]{2}))-(?P<month>([0-9]{1,2}))-(?P<year>([0-9]{4}))')
        date = RE_DATE.match(date_in)
        return (f'число: {int(date.groupdict().get("day"))}\n'
                f'месяц: {int(date.groupdict().get("month"))}\n'
                f'год: {int(date.groupdict().get("year"))}')

    @staticmethod
    def validation(date_in):
        try:
            datetime.datetime.strptime(date_in, '%d-%m-%Y')
        except ValueError as err:
            return print(f'ValueError: {err}\nДата должна быть формата: DD-MM-YYYY')
        return date_in


print(Data.extracting_number('08-03-2020'))
print(Data.validation('08-03-2021'))
