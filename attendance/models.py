from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.

class Attend(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.student.username) + " " + str(self.datetime)[:19]
