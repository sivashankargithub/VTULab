from django import forms
from app1.models import Students,Course

class Inputform1(forms.ModelForm):
    class Meta:
        model=Students
        fields='__all__'

class Inputform2(forms.ModelForm):
    class Meta:
        model=Course
        fields='__all__'

class Inputform3(forms.Form):
    input1=forms.CharField(max_length=20, label='Enter course_id')