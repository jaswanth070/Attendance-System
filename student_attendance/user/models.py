from django.db import models

class Staff(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20, blank=True,null=True)
    
    def __str__(self):
        return self.full_name


class Student(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    full_name = models.CharField(max_length=150)
    assigned_staff = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, blank=True)
    phone = models.CharField(max_length=20)
    
    def __str__(self):
        return self.full_name
