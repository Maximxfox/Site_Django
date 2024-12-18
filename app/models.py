from django.db import models


class Job(models.Model):
    name = models.CharField(max_length=255)
    key_skills = models.TextField()
    salary= models.FloatField(null=True, blank=True)
    area_name = models.CharField(max_length=255)
    published_at = models.CharField(max_length=4)


    class Meta:
        db_table = 'job'


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


