from django import forms
from app1.models import Student

class InputForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'