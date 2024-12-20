import pandas as pd
import requests
import json
from django.shortcuts import render
from .models import *


def index_page(request):
    return render(request, 'index.html')


def stats_page(request):
    selected_year = request.GET.get('published_at', 2015)
    salary_year = General_Job_Year_Salary.objects.all()
    salary_year = [{'published_at': int((float(record.published_at))), 'salary': int(record.salary)} for record in salary_year]
    photo_salary_year = Photo.objects.filter(title='Общая статистика зарплат по годам')
    count_year = General_Job_Year_Count.objects.all()
    count_year = [{'published_at': int((float(record.published_at))), 'count': record.count} for record in count_year]
    photo_count_year = Photo.objects.filter(title='Общая статистика количества по годам')
    salary_area = General_Job_Area_Salary.objects.all()
    salary_area = [{'area_name': record.area_name, 'salary': int(record.salary)} for record in salary_area]
    photo_salary_area = Photo.objects.filter(title='Общая статистика зарплат по городам')
    count_area = General_Job_Area_Count.objects.all()
    count_area = [{'area_name': record.area_name, 'count': record.count} for record in count_area]
    photo_count_area = Photo.objects.filter(title='Общая статистика количества по городам')
    skills = General_Job_Skills.objects.filter(published_at=selected_year).order_by('count')
    skills = [{'key_skill': record.key_skill,'published_at': int((float(record.published_at))), 'count': record.count} for record in skills]
    all_years = list(General_Job_Skills.objects.order_by('published_at').values_list('published_at', flat=True).distinct())
    photo_skills = Photo.objects.filter(title='general_'+str(selected_year))
    return render(request, 'stats.html', {'salary_year': salary_year,
                                          'count_year': count_year,
                                          'salary_area': salary_area,
                                          'count_area': count_area,
                                          'skills': skills,
                                          'photo_salary_year': photo_salary_year,
                                          'photo_count_year': photo_count_year,
                                          'photo_salary_area': photo_salary_area,
                                          'photo_count_area': photo_count_area,
                                          'photo_skills': photo_skills,
                                          'selected_year': selected_year,
                                          'all_years': all_years})


def relevance_page(request):
    salary = Job_Year_Salary.objects.all()
    salary = [{'published_at': int((float(record.published_at))), 'salary': int(record.salary)} for record in salary]
    photo_salary = Photo.objects.filter(title='Статистика зарплат по годам')
    count = Job_Year_Count.objects.all()
    count = [{'published_at': int((float(record.published_at))), 'count': record.count} for record in count]
    photo_count = Photo.objects.filter(title='Статистика количества по годам')
    return render(request, 'relevance.html', {'salary': salary, 'count': count, 'photo_salary': photo_salary, 'photo_count': photo_count})


def geography_page(request):
    salary = Job_Area_Salary.objects.all()
    salary = [{'area_name': record.area_name, 'salary': int(record.salary)} for record in salary]
    photo_salary = Photo.objects.filter(title='Статистика зарплат по городам')
    count = Job_Area_Count.objects.all()
    count = [{'area_name': record.area_name, 'count': record.count} for record in count]
    photo_count = Photo.objects.filter(title='Статистика количества по городам')
    return render(request, 'geography.html', {'salary': salary, 'count': count, 'photo_salary': photo_salary, 'photo_count': photo_count})


def skills_page(request):
    selected_year = request.GET.get('published_at', 2015)
    skills = Job_Skills.objects.filter(published_at=selected_year).order_by('count')
    skills = [{'key_skill': record.key_skill,'published_at': int((float(record.published_at))), 'count': record.count} for record in skills]
    all_years = list(Job_Skills.objects.order_by('published_at').values_list('published_at', flat=True).distinct())
    photo = Photo.objects.filter(title=str(selected_year))
    return render(request, 'skills.html',{'skills': skills, 'selected_year': selected_year, 'all_years': all_years, 'photo': photo} )


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
        else:
            salary = 'Не указано'
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


def last_vacancies_page(request):
    Vacancy_From_HH.objects.all().delete()
    vacancy_list = main()
    for vacancy in vacancy_list:
        Vacancy_From_HH.objects.create(
            name=vacancy['Название вакансии'],
            description=vacancy['Описание'],
            skills=vacancy['Навыки'],
            company=vacancy['Компания'],
            salary=vacancy['Оклад'],
            area=vacancy['Название региона'],
            published_at=vacancy['Дату публикации вакансии']
        )
    vacancies = Vacancy_From_HH.objects.all()
    return render(request, 'last_vacancies.html', {'vacancies': vacancies})
