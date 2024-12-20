from django.db import models
import os


class General_Job_Year_Salary(models.Model):
    salary = models.FloatField()
    published_at = models.CharField(max_length=4)


    def __str__(self):
        return f"{self.published_at}"


    class Meta:
        db_table = 'general_year_salary'
        verbose_name = "Зарплата"
        verbose_name_plural = "Общая зарплата от года"


class General_Job_Year_Count(models.Model):
    count = models.IntegerField()
    published_at = models.CharField(max_length=4)


    def __str__(self):
        return f"{self.published_at}"


    class Meta:
        db_table = 'general_year_count'
        verbose_name = "Количество"
        verbose_name_plural = "Общее Количество от года"


class General_Job_Area_Salary(models.Model):
    salary = models.FloatField(null=True, blank=True)
    area_name = models.CharField(max_length=255)


    def __str__(self):
        return f"{self.area_name}"


    class Meta:
        db_table = 'general_area_salary'
        verbose_name = "Зарплата"
        verbose_name_plural = "Общая Зарплата от места"


class General_Job_Area_Count(models.Model):
    count = models.FloatField(null=True, blank=True)
    area_name = models.CharField(max_length=255)


    def __str__(self):
        return f"{self.area_name}"


    class Meta:
        db_table = 'general_area_count'
        verbose_name = "Доля вакансий"
        verbose_name_plural = "Общая доля от вакансий города"


class General_Job_Skills(models.Model):
    count = models.IntegerField()
    key_skill = models.CharField(max_length=100)
    published_at = models.CharField(max_length=4)


    def __str__(self):
        return f"{self.published_at} {self.key_skill}"


    class Meta:
        db_table = 'general_skills'
        verbose_name = "Навык"
        verbose_name_plural = "Общие скиллы"


class Job_Year_Salary(models.Model):
    salary = models.FloatField()
    published_at = models.CharField(max_length=4)


    def __str__(self):
        return f"{self.published_at}"


    class Meta:
        db_table = 'year_salary'
        verbose_name = "Зарплата"
        verbose_name_plural = "Зарплата от года"


class Job_Year_Count(models.Model):
    count = models.IntegerField()
    published_at = models.CharField(max_length=4)


    def __str__(self):
        return f"{self.published_at}"


    class Meta:
        db_table = 'year_count'
        verbose_name = "Количество"
        verbose_name_plural = "Количество от года"


class Job_Area_Salary(models.Model):
    salary = models.FloatField(null=True, blank=True)
    area_name = models.CharField(max_length=255)


    def __str__(self):
        return f"{self.area_name}"


    class Meta:
        db_table = 'area_salary'
        verbose_name = "Зарплата"
        verbose_name_plural = "Зарплата от места"


class Job_Area_Count(models.Model):
    count = models.FloatField(null=True, blank=True)
    area_name = models.CharField(max_length=255)


    def __str__(self):
        return f"{self.area_name}"


    class Meta:
        db_table = 'area_count'
        verbose_name = "Доля вакансий"
        verbose_name_plural = "Доля от вакансий города"


class Job_Skills(models.Model):
    count = models.IntegerField()
    key_skill = models.CharField(max_length=100)
    published_at = models.CharField(max_length=4)


    def __str__(self):
        return f"{self.published_at} {self.key_skill}"


    class Meta:
        db_table = 'skills'
        verbose_name = "Навык"
        verbose_name_plural = "Скиллы"


class Vacancy_From_HH(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    skills = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    salary = models.CharField(max_length=255, blank=True, null=True)
    area = models.CharField(max_length=255)
    published_at = models.DateTimeField()


    def __str__(self):
        return f"{self.name} {self.published_at}"


    class Meta:
        db_table = 'vacancy_from_hh'
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии из HH"


class Photo(models.Model):
    image = models.ImageField(upload_to='')
    title = models.CharField(max_length=200)


    def __str__(self):
        return self.title


    def delete(self, *args,**kwargs):
        if self.image:
             storage, path = self.image.storage, self.image.path
             if os.path.exists(path):
                storage.delete(path)
        super().delete(*args, **kwargs)


    def save(self, *args, **kwargs):
        try:
            old_photo = Photo.objects.get(title=self.title)
            if old_photo.image and self.image != old_photo.image:
                storage, path = old_photo.image.storage, old_photo.image.path
                if os.path.exists(path):
                    storage.delete(path)
        except Photo.DoesNotExist:
            pass
        super().save(*args, **kwargs)


    class Meta:
        db_table = 'photos'
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'