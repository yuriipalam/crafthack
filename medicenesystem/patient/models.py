from django.db import models
from django.contrib.auth.models import User


class Pillow(models.Model):
    name = models.CharField(max_length=100, null=False)
    start_date = models.DateField(auto_now=True)
    finish_date = models.DateField(null=False)
    times_per_day = models.IntegerField(null=False)

    def __str__(self):
        return self.name


class Instruction(models.Model):
    pillows = models.ManyToManyField(Pillow)
    description = models.TextField(max_length=1000, null=False)

    def __str__(self):
        return "Instrudction " + str(self.id)


class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    birth_date = models.DateField(null=False)
    address = models.CharField(max_length=100, null=False)
    social_number = models.IntegerField(unique=True)
    instruction = models.ForeignKey(Instruction, on_delete=models.CASCADE)
    disease = models.CharField(max_length=100, null=False, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
