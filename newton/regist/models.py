from django.db import models
from django.utils import timezone

class Regist(models.Model):
    name = models.CharField(max_length=50, default="Иван")
    surname = models.CharField(max_length=50, default="Иванов")
    birthday = models.DateField()
    email = models.CharField(max_length=50, default="ivanov@gmail.com")
    password = models.CharField(max_length=50, default="********")

    def __str__(self):
        return self.name, self.surname, self.birthday, self.email
    

    