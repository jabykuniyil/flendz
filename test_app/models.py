from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.BigIntegerField(primary_key=True)
    date_of_birth = models.DateField()
    
class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    mark = models.IntegerField()