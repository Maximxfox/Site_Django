import pandas as pd
import requests
import json


def get_current_and_yesterday_dates():
    current_date = pd.Timestamp('today')
    yesterday_date = current_date - pd.Timedelta(days=1)
    current_date = current_date.strftime('%Y-%m-%dT%H:%M:%S')
    yesterday_date = yesterday_date.strftime('%Y-%m-%dT%H:%M:%S')
    return current_date, yesterday_date


def get_vacancy_details(vacancy_id):
    vacancy_url = f"https://api.hh.ru/vacancies/{vacancy_id}"
    response = requests.get(vacancy_url)
    return response.json()


def calculate_average_salary(salary_from, salary_to):
    if pd.isna(salary_to) and pd.isna(salary_from):
        return None
    elif pd.isna(salary_to):
        return salary_from
    elif pd.isna(salary_from):
        return salary_to
    else:
        return (salary_from + salary_to) / 2.0


def process_vacancies(vacancies):
    vacancy_list = []
    for item in vacancies['items']:
        vacancy_id = item['id']
        details = get_vacancy_details(vacancy_id)
        if item['salary'] is not None:
            salary_from = item['salary']['from']
            salary_to = item['salary']['to']
            salary = calculate_average_salary(salary_from, salary_to)
        vacancy = {
            "Название вакансии": item['name'],
            "Описание": details.get('description', ''),
            "Навыки": ', '.join([skill['name'] for skill in details.get('key_skills', [])]),
            "Компания": item['employer']['name'],
            "Оклад": f"{salary} {item['salary']['currency']}" if item.get('salary') else 'Не указано',
            "Название региона": item['area']['name'],
            "Дату публикации вакансии": item['published_at']
        }
        vacancy_list.append(vacancy)
    return vacancy_list


def main():
    BASE_URL = 'https://api.hh.ru/vacancies'
    current_date, yesterday_date = get_current_and_yesterday_dates()
    params = {
        'per_page': 10,
        'page': 0,
        'text': 'NAME:(php or пхп or рнр)',
        'date_from': yesterday_date,
        'date_to': current_date,
        'order_by': "publication_time",
    }
    response = requests.get(BASE_URL, params=params)
    data = response.content.decode()
    vacancies = json.loads(data)
    return process_vacancies(vacancies)