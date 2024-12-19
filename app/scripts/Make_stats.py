import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def find_salary_by_year(df):
    salary_by_year = df.groupby('published_at')['salary'].mean().reset_index()
    return salary_by_year


def make_img_salary_by_year(salary_by_year):
    plt.figure(figsize=(15, 10))
    plt.plot(salary_by_year.index, salary_by_year.values, marker='o', linestyle='-', color='b')
    plt.title('Динамика уровня зарплат по годам (в рублях)', fontsize=14)
    plt.xlabel('Год', fontsize=12)
    plt.ylabel('Средняя зарплата (руб.)', fontsize=12)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('app/scripts/relevance/salary.png')



def find_vacancies_by_year(df):
    vacancies_by_year = df.groupby('published_at')['name'].count().reset_index()
    return vacancies_by_year


def make_img_vacancies_by_year(vacancies_by_year):
    plt.figure(figsize=(15, 10))
    plt.plot(vacancies_by_year.index, vacancies_by_year.values, marker='o', linestyle='-', color='g')
    plt.title('Динамика количества вакансий по годам', fontsize=14)
    plt.xlabel('Год', fontsize=12)
    plt.ylabel('Количество вакансий', fontsize=12)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('app/scripts/relevance/count.png')


def find_salary_by_city(df):
    salary_by_city = df.groupby('area_name')['salary'].mean()
    salary_by_city = salary_by_city.sort_values(ascending=False)[:100].reset_index()
    return salary_by_city


def make_img_salary_by_city(salary_by_city):
    plt.figure(figsize=(15, 10))
    salary_by_city.plot(kind='bar', color='b')
    plt.title('Уровень зарплат по городам (в рублях)', fontsize=14)
    plt.xlabel('Город', fontsize=12)
    plt.ylabel('Средняя зарплата (руб.)', fontsize=12)
    plt.xticks(rotation=90)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('app/scripts/geography/salary.png')


def find_vacancies_by_city(df):
    vacancies_by_city = df.groupby('area_name')['name'].count()
    total_vacancies = vacancies_by_city.sum()
    vacancies_by_city = vacancies_by_city / total_vacancies
    vacancies_by_city = vacancies_by_city.sort_values(ascending=False)[:100].reset_index()
    return vacancies_by_city


def make_img_vacancies_by_city(vacancies_by_city):
    plt.figure(figsize=(15, 10))
    vacancies_by_city.plot(kind='bar', color='g')
    plt.title('Доля вакансий по городам', fontsize=14)
    plt.xlabel('Город', fontsize=12)
    plt.ylabel('Доля вакансий', fontsize=12)
    plt.xticks(rotation=90)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('app/scripts/geography/count.png')


def parse_skills(x):
    if isinstance(x, str):
        return [skill.strip() for skill in x.split(', ')]
    else:
        return np.nan


def generate_skills_by_year(df):
    skills_by_year = df
    skills_by_year['key_skills'] = skills_by_year['key_skills'].apply(parse_skills)
    skills_by_year = df.explode('key_skills').reset_index(drop=True)
    skills_by_year.dropna(subset=['key_skills'], inplace=True)
    skills_by_year = skills_by_year.groupby(['published_at', 'key_skills']).agg(count=('key_skills', 'size')).reset_index()
    skills_by_year = (skills_by_year
        .sort_values(['published_at', 'count'], ascending=[True, False])
        .groupby('published_at')
        .head(20)
        .reset_index(drop=True)
    )
    return skills_by_year


def make_img_skills_by_year(skills_by_year):
    years = skills_by_year['published_at'].unique()
    for year in years:
        plt.figure(figsize=(15, 10))
        year_data = skills_by_year[skills_by_year['published_at'] == year]
        plt.barh(year_data['key_skills'], year_data['count'], color='skyblue', edgecolor='black')
        plt.title(f'ТОП-20 скиллов за {year}')
        plt.xlabel('Востребованность')
        plt.ylabel('Навыки')
        plt.tight_layout()
        plt.savefig(f'top-20/{year}.png')