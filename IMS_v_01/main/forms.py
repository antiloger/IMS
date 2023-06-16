from django import forms
from .models import Student, Teacher


class Studentform(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['std_ID', 'std_fname', 'std_lname', 'std_bod', 'std_email', 'std_pnum', 'std_nic']


class Teacherform(forms.ModelForm):
    class Meta:
        model = Teacher
        fields =['t_ID', 't_fname', 't_lname', 't_bod', 't_email', 't_pnum', 't_nic']
