import pandas as pd
import requests
import json
from django.shortcuts import render
from .models import *
from app.scripts.find_new_vacancies import main


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