from django.contrib import admin
from mydbapp.models import Employees
from mydbapp.models import Departments
from mydbapp.models import Salaries

# Register your models here.
admin.site.register(Employees)
admin.site.register(Departments)
admin.site.register(Salaries)
