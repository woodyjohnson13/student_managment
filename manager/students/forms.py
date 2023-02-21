from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['student_number','student_name','student_last_name','email','field_of_study','gpa']
        
        labels={'student_number':'Student Number',
                'student_name':'Student Name',
                'student_last_name':'Student Last Name',
                'email':'Email',
                'field_of_study':'Field of Study',
                'gpa':'GPA'}
        
        widgets={'student_number':forms.NumberInput(attrs={'class':'form-control'}),
                'student_name':forms.TextInput(attrs={'class':'form-control'}),
                'student_last_name':forms.TextInput(attrs={'class':'form-control'}),
                'email':forms.EmailInput(attrs={'class':'form-control'}),
                'field_of_study':forms.TextInput(attrs={'class':'form-control'}),
                'gpa':forms.NumberInput(attrs={'class':'form-control'})}