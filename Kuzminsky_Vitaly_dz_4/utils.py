import sys

import requests


def currency_rates(code: str) -> float:
    """
    Returns the exchange rate of the currency 'code` in relation to the ruble
    (Возвращает курс валюты `code` по отношению к рублю)

    :param code: str -- The argument currency code of 3 characters (Аргумент код валюты из 3 символов).
    :return: float -- The exchange rate of a given currency to 1 ruble (Курс заданной валюты к 1 рублю).
    :return: None -- If the value is not found (Если значение не найдено).

    """


    response_cbr = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    cbr_text = response_cbr.text
    id_currency = cbr_text.find(code.upper())
    if id_currency != -1:
        cbr_text = cbr_text[id_currency:cbr_text.find('</Value>', id_currency)]
        nominal_value = float(cbr_text[cbr_text.find('<Nominal>') + 9: cbr_text.find('</Nominal>')].replace(',', '.'))
        value_rub = float(cbr_text[cbr_text.find('<Value>') + 7:].replace(',', '.'))
        response_cbr.close()
    else:
        response_cbr.close()
        return
    result_value = round(value_rub / nominal_value, 4)
    return result_value


if __name__ == '__main__':
    print(sys.code)
    sys.exit(currency_rates(sys.code))