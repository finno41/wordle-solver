from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username

class Score(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateField()
    score = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')


class Word(models.Model):
    name = models.CharField(max_length=5)
