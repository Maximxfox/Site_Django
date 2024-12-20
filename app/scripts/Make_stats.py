import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def find_salary_by_year(df):
    salary_by_year = df.groupby('published_at')['salary'].mean().reset_index().astype(int)
    return salary_by_year


def make_img_salary_by_year(salary_by_year):
    plt.figure(figsize=(15, 10))
    plt.plot(salary_by_year['published_at'], salary_by_year['salary'], marker='o', linestyle='-', color='b')
    plt.title('Динамика уровня зарплат по годам (в рублях)', fontsize=14)
    plt.xlabel('Год', fontsize=12)
    plt.ylabel('Средняя зарплата (руб.)', fontsize=12)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('relevance/general_salary.png')



def find_vacancies_by_year(df):
    vacancies_by_year = df.groupby('published_at')['name'].count().reset_index()
    return vacancies_by_year


def make_img_vacancies_by_year(vacancies_by_year):
    plt.figure(figsize=(15, 10))
    plt.plot(vacancies_by_year['published_at'], vacancies_by_year['name'], marker='o', linestyle='-', color='g')
    plt.title('Динамика количества вакансий по годам', fontsize=14)
    plt.xlabel('Год', fontsize=12)
    plt.ylabel('Количество вакансий', fontsize=12)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('relevance/general_count.png')


def find_salary_by_city(df):
    total_vacancies = len(df)
    salary_area = (
        df
        .groupby('area_name')
        .agg({'salary': 'mean', 'name': 'count'})
        .assign(perc=lambda df: df['name'] / total_vacancies)
        .sort_values(['salary', 'area_name'], ascending=[False, True])
        .query('perc >= 0.01')
        .astype(int)
        .reset_index()
    )
    return salary_area


def make_img_salary_by_city(salary_by_city):
    plt.figure(figsize=(15, 10))
    plt.bar(salary_by_city['area_name'], salary_by_city['salary'], color='b', width=0.5)
    plt.title('Уровень зарплат по городам (в рублях)', fontsize=14)
    plt.xlabel('Город', fontsize=12)
    plt.ylabel('Средняя зарплата (руб.)', fontsize=12)
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig('geography/salary.png')


def find_vacancies_by_city(df):
    total_vacancies = len(df)
    vacancies_by_city = (
        df
        .groupby('area_name')
        .agg({'name': 'count'})
        .assign(perc=lambda df: df['name'] / total_vacancies)
        .round(4)
        .sort_values(['perc', 'area_name'], ascending=[False, True])
        .query('perc >= 0.01')
        .reset_index()
    )
    return vacancies_by_city


def make_img_vacancies_by_city(vacancies_by_city):
    plt.figure(figsize=(15, 10))
    plt.bar(vacancies_by_city['area_name'], vacancies_by_city['perc'], color='g', width=0.5)
    plt.title('Доля вакансий по городам', fontsize=14)
    plt.xlabel('Город', fontsize=12)
    plt.ylabel('Доля вакансий', fontsize=12)
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig('geography/general_count.png')



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
        plt.savefig(f'top-20/general_{year}.png')
