# Generated by Django 5.1.4 on 2024-12-20 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='General_Job_Area_Count',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.FloatField(blank=True, null=True)),
                ('area_name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Доля вакансий',
                'verbose_name_plural': 'Общаий процент города',
                'db_table': 'general_area_count',
            },
        ),
        migrations.CreateModel(
            name='General_Job_Area_Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.FloatField(blank=True, null=True)),
                ('area_name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Зарплата',
                'verbose_name_plural': 'Общая Зарплата от места',
                'db_table': 'general_area_salary',
            },
        ),
        migrations.CreateModel(
            name='General_Job_Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('key_skill', models.CharField(max_length=100)),
                ('published_at', models.CharField(max_length=4)),
            ],
            options={
                'verbose_name': 'Навык',
                'verbose_name_plural': 'Общие скиллы',
                'db_table': 'general_skills',
            },
        ),
        migrations.CreateModel(
            name='General_Job_Year_Count',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('published_at', models.CharField(max_length=4)),
            ],
            options={
                'verbose_name': 'Количество',
                'verbose_name_plural': 'Общее Количество от года',
                'db_table': 'general_year_count',
            },
        ),
        migrations.CreateModel(
            name='General_Job_Year_Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.FloatField()),
                ('published_at', models.CharField(max_length=4)),
            ],
            options={
                'verbose_name': 'Зарплата',
                'verbose_name_plural': 'Общая зарплата от года',
                'db_table': 'general_year_salary',
            },
        ),
        migrations.CreateModel(
            name='Job_Area_Count',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.FloatField(blank=True, null=True)),
                ('area_name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Доля вакансий',
                'verbose_name_plural': 'Процент города',
                'db_table': 'area_count',
            },
        ),
        migrations.CreateModel(
            name='Job_Area_Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.FloatField(blank=True, null=True)),
                ('area_name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Зарплата',
                'verbose_name_plural': 'Зарплата от места',
                'db_table': 'area_salary',
            },
        ),
        migrations.CreateModel(
            name='Job_Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('key_skill', models.CharField(max_length=100)),
                ('published_at', models.CharField(max_length=4)),
            ],
            options={
                'verbose_name': 'Навык',
                'verbose_name_plural': 'Скиллы',
                'db_table': 'skills',
            },
        ),
        migrations.CreateModel(
            name='Job_Year_Count',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('published_at', models.CharField(max_length=4)),
            ],
            options={
                'verbose_name': 'Количество',
                'verbose_name_plural': 'Количество от года',
                'db_table': 'year_count',
            },
        ),
        migrations.CreateModel(
            name='Job_Year_Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.FloatField()),
                ('published_at', models.CharField(max_length=4)),
            ],
            options={
                'verbose_name': 'Зарплата',
                'verbose_name_plural': 'Зарплата от года',
                'db_table': 'year_salary',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Фотография',
                'verbose_name_plural': 'Фотографии',
                'db_table': 'photos',
            },
        ),
        migrations.CreateModel(
            name='Vacancy_From_HH',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('skills', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('salary', models.CharField(blank=True, max_length=255, null=True)),
                ('area', models.CharField(max_length=255)),
                ('published_at', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии из HH',
                'db_table': 'vacancy_from_hh',
            },
        ),
    ]
