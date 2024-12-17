# Generated by Django 5.1.4 on 2024-12-17 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('key_skills', models.TextField()),
                ('salary', models.FloatField(blank=True, null=True)),
                ('area_name', models.CharField(max_length=255)),
                ('published_at', models.CharField(max_length=4)),
            ],
            options={
                'db_table': 'app_job',
            },
        ),
    ]
