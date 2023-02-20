from django.db import models

# Create your models here.

class Student(models.Model):
    student_number=models.PositiveBigIntegerField(primary_key=True)
    student_name=models.CharField(max_length=50)
    student_last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    field_of_study=models.CharField(max_length=50)
    gpa=models.FloatField()
    
    def __str__(self):
        return f"Student {self.student_name} {self.student_last_name}, {self.field_of_study}, {self.gpa}"