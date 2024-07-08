from django.db import models


class Course(models.Model):
    course=models.CharField(max_length=25)

    def __str__(self):
        return self.course
     
class Students(models.Model):
    name=models.CharField(max_length=100)
    course=models.ManyToManyField(Course)

    def __str__(self):
        return self.name


