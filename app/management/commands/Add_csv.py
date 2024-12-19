import pandas as pd
from django.core.management.base import BaseCommand
from django.conf import settings
from app.models import *
from app.scripts.Make_stats import find_salary_by_year, find_vacancies_by_year, find_salary_by_city, find_vacancies_by_city, generate_skills_by_year
import os


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        df = pd.read_csv(settings.CSV_DATA_PATH)
        for index, row in find_salary_by_year(df).iterrows():
            Job_Year_Salary.objects.create(
                salary=row['salary'],
                published_at=row['published_at'],
            )
        for index, row in find_vacancies_by_year(df).iterrows():
            Job_Year_Count.objects.create(
                count=row['name'],
                published_at=row['published_at'],
            )
        for index, row in find_salary_by_city(df).iterrows():
            Job_Area_Salary.objects.create(
                salary=row['salary'],
                area_name=row['area_name'],
            )
        for index, row in find_vacancies_by_city(df).iterrows():
            Job_Area_Count.objects.create(
                count=row['name'],
                area_name=row['area_name'],
            )
        for index, row in generate_skills_by_year(df).iterrows():
            Job_Skills.objects.create(
                count = row['count'],
                key_skill=row['key_skills'],
                published_at=row['published_at'],
            )


