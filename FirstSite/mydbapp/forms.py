from django import forms
from mydbapp.models import Employees, Departments

import datetime

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

class EmployeeForm(forms.ModelForm):
    emp_no      = forms.IntegerField(help_text="Enter employee number: ")
    birth_date  = forms.DateField(help_text="Enter birth date: ")
    first_name  = forms.CharField(max_length=14, help_text="Enter frist name: ")
    last_name   = forms.CharField(max_length=16, help_text="Enter last name: ")
    gender      = forms.CharField(max_length=1,widget=forms.Select(choices=GENDER_CHOICES), help_text="Select gender: ")
    hire_date   = forms.DateField(initial=datetime.date.today(),help_text="Enter hire date: ")
    class Meta:
        model = Employees
        fields = '__all__'

class EmployeeGetForm(forms.ModelForm):
    emp_no      = forms.IntegerField(help_text="Enter employee number: ")
    birth_date  = forms.DateField(help_text="Enter birth date: ")
    first_name  = forms.CharField(max_length=14, help_text="Enter frist name: ")
    last_name   = forms.CharField(max_length=16, help_text="Enter last name: ")
    gender      = forms.CharField(max_length=1,widget=forms.Select(choices=GENDER_CHOICES), help_text="Select gender: ")
    hire_date   = forms.DateField(help_text="Enter hire date: ")
    class Meta:
        model = Employees
        fields = '__all__'

class DepartmentForm(forms.ModelForm):
    dept_no     = forms.CharField(max_length=4)
    dept_name   = forms.CharField(max_length=40)
    class Meta:
        model = Departments
