import pandas as pd
import requests
import csv
from lxml import etree


BASE_URL = 'https://www.cbr.ru/scripts/XML_daily.asp'
all_currency = ['BYR', 'USD', 'EUR', 'KZT', 'UAH', 'AZN', 'KGS', 'UZS', 'GEL']


def prepare_currency_data(tree, currency):
    need_info = tree.xpath(f"//Valute[CharCode='{currency}']")
    if not need_info:
        return None
    value = float(need_info[0].find('Value').text.replace(',', '.'))
    nominal = int(need_info[0].find('Nominal').text)
    return round(value / nominal, 8)


def find_currency_data(date, all_currency):
    response = requests.get(f'{BASE_URL}?date_req={date.strftime("%d/%m/%Y")}')
    tree = etree.fromstring(response.content)
    row = [date.strftime('%Y-%m')]
    for currency in all_currency:
        row.append(prepare_currency_data(tree, currency))
    return row


def main():
    current_date = pd.to_datetime('2003.01.01')
    end_date = pd.to_datetime('2024.12.01')
    offset = pd.DateOffset(months=1)
    with open('csv_data/currency.csv', mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(['date'] + all_currency)
        while current_date <= end_date:
            row = find_currency_data(current_date, all_currency)
            writer.writerow(row)
            current_date += offset


if __name__ == "__main__":
    main()