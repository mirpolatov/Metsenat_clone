from django.contrib.auth.models import AbstractUser, User
from django.core.validators import RegexValidator
from django.db import models
from django.db.models import Choices, CASCADE
from rest_framework.exceptions import ValidationError


# Create your models here.

class Users(AbstractUser):
    fullname = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)


class Sponsor(models.Model):
    user = models.ForeignKey('Users', on_delete=CASCADE)
    fullname = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, default='unknown')
    summa = models.PositiveIntegerField()
    tashkilot_nomi = models.CharField(max_length=100, default='unknown')
    ariza = models.BooleanField(default=False)
    created_at = models.TimeField(auto_now=True)
    # student = models.ForeignKey('Student', on_delete=CASCADE)
    # payment_type = models.CharField(max_length=20, choices=CHOICES)


class Student(models.Model):
    user = models.ForeignKey('Users', on_delete=CASCADE, related_name='user')
    fullname = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=50)
    otm = models.CharField(max_length=100)
    student_category = models.CharField(max_length=50)
    summa = models.PositiveIntegerField()
