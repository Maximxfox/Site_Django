from django.db import models


class Job(models.Model):
    name = models.CharField(max_length=255)
    key_skills = models.TextField()
    salary= models.FloatField(null=True, blank=True)
    area_name = models.CharField(max_length=255)
    published_at = models.CharField(max_length=4)

    class Meta:
        db_table = 'app_job'