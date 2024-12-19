import pandas as pd
import numpy as np


def find_rate(row, df_currency):
    currency = row['salary_currency']
    if currency == 'RUR':
        return row['salary']
    else:
        date = row['date']
        if date in df_currency.index and currency in df_currency.columns:
            return row['salary'] * df_currency.at[date, currency]
        return None


def find_data(data, df_currency):
    data['date'] = pd.to_datetime(data['published_at'], errors='coerce', utc=True).dt.strftime('%Y-%m')
    data['salary'] = data.apply(lambda row: row[['salary_from', 'salary_to']].mean(), axis=1)
    data['salary'] = data.apply(lambda row: find_rate(row, df_currency), axis=1)
    data['key_skills'] = data['key_skills'].apply(lambda x: ', '.join([skill.strip() for skill in str(x).split('\n')]) if isinstance(x, str) else np.nan)
    data['published_at'] = pd.to_datetime(data['published_at'], errors='coerce', utc=True).dt.strftime('%Y')
    return data


def update(data, output_file):
    data = data[['name', 'key_skills', 'salary', 'area_name', 'published_at']]
    data = data[(data['salary'] <= 10_000_000) | (data['salary'].isna())]
    data.to_csv(output_file, index=False)


def main():
    df_currency = pd.read_csv('csv_data/currency.csv', index_col='date')
    csv_merged = pd.read_csv('csv_data/vacancies_2024.csv')
    php_keywords = ['php', 'пхп', 'рнр']
    csv_merged = csv_merged[csv_merged['name'].str.contains('|'.join(php_keywords), case=False)]
    csv_merged = find_data(csv_merged, df_currency)
    output_file = 'csv_data/updated_vacancies.csv'
    update(csv_merged, output_file)


if __name__ == "__main__":
    main()
