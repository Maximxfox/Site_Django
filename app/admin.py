from django.contrib import admin
from .models import *


admin.site.register(Job)
admin.site.register(Job_Year_Salary)
admin.site.register(Job_Year_Count)
admin.site.register(Job_Area_Salary)
admin.site.register(Job_Area_Count)
admin.site.register(Job_Skills)
admin.site.register(Vacancy_From_HH)

