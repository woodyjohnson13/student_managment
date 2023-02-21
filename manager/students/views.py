from django.shortcuts import render
from .models import Student
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import StudentForm
# Create your views here.

def index(request):
    return render(request, 'students/index.html',{
        'students': Student.objects.all(),
    })
    
def view_student(request, id):
    student=Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method=='POST':
        form=StudentForm(request.POST)
        
        if form.is_valid():
            new_student_number=form.cleaned_data['student_number']
            new_student_name=form.cleaned_data['student_name']
            new_student_last_name=form.cleaned_data['student_last_name']
            new_student_email=form.cleaned_data['email']
            new_student_field=form.cleaned_data['field_of_study']
            new_student_gpa=form.cleaned_data['gpa']
            
            new_student=Student(
                student_number=new_student_number,
                student_name=new_student_name,
                student_last_name=new_student_last_name,
                email=new_student_email,
                field_of_study=new_student_field,
                gpa=new_student_gpa
            )
            
            new_student.save()
            
            return render(request, 'students/add.html',{
                'form':StudentForm (),
                'success':True,
            })
                          
        else:
            form=StudentForm()