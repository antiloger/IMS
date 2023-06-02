from django import forms
from .models import Student


class Studentform(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['std_ID', 'std_fname', 'std_lname', 'std_bod', 'std_email', 'std_pnum', 'std_nic']