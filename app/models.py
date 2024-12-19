from django.db import models


class Job(models.Model):
    name = models.CharField(max_length=255)
    key_skills = models.CharField(max_length=1000, null=True, blank=True)
    salary = models.FloatField(null=True, blank=True)
    area_name = models.CharField(max_length=255)
    published_at = models.CharField(max_length=4)


    class Meta:
        db_table = 'job'


class Job_Year_Salary(models.Model):
    salary = models.FloatField()
    published_at = models.CharField(max_length=4)


    class Meta:
        db_table = 'year_salary'


class Job_Year_Count(models.Model):
    count = models.IntegerField()
    published_at = models.CharField(max_length=4)


    class Meta:
        db_table = 'year_count'


class Job_Area_Salary(models.Model):
    salary = models.FloatField(null=True, blank=True)
    area_name = models.CharField(max_length=255)


    class Meta:
        db_table = 'area_salary'


class Job_Area_Count(models.Model):
    count = models.FloatField(null=True, blank=True)
    area_name = models.CharField(max_length=255)


    class Meta:
        db_table = 'area_count'


class Job_Skills(models.Model):
    count = models.IntegerField()
    key_skill = models.CharField(max_length=100)
    published_at = models.CharField(max_length=4)


    class Meta:
        db_table = 'skills'


class Vacancy_From_HH(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    skills = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    salary = models.CharField(max_length=255, blank=True, null=True)
    area = models.CharField(max_length=255)
    published_at = models.DateTimeField()


    class Meta:
        db_table = 'vacancy_from_hh'


