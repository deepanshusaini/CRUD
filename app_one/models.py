from django.db import models
from django.urls import reverse
# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=50)
    principle = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("app_one:student_details",kwargs={'pk':self.pk})


class Student(models.Model):
    student_name = models.CharField(max_length=50)
    school = models.ForeignKey(School,related_name='students',on_delete=models.CASCADE)
    def __str__(self):
        return self.student_name