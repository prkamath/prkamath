from __future__ import unicode_literals

from django.db import models


class School(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Student(models.Model):
    name=models.CharField(max_length=20)
    school=models.ManyToManyField(School)
    def __str__(self):
        return self.name + " " + str(self.school)


class School1(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Student1(models.Model):
    name=models.CharField(max_length=20)
    school1=models.ForeignKey(School1)
    def __str__(self):
        return self.name + " " + str(self.school1)


class School2(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Student2(models.Model):
    name=models.CharField(max_length=20)
    school2=models.OneToOneField(School2)
    def __str__(self):
        return self.name + " " + str(self.school2)