from django.db import models
# very important line to put
from django.urls import reverse

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=120)
    principal = models.CharField(max_length=120)
    Location = models.CharField(max_length=120)

    def __str__(self):
        return self.name

    # creating a function that will take in user's info from the forms and retirect the user to another page
    def get_absolute_url(self):
        return reverse("AdvanceCBV_App:detail",kwargs={'pk':self.pk})


class Student(models.Model):
    Name = models.CharField(max_length=120)
    age = models.PositiveIntegerField()
    school= models.ForeignKey(School, related_name='students', on_delete=models.CASCADE)

    def __str__(self):
        return self.Name
