from django.db import models

# Create your models here.


class Group:

     id = models.BigIntegerField(primary_key=True)
     enabled_sup = models.OneToOneField(blank=True)
     teacher = models.ForeignKey()

class Student:

    name = models.CharField()
    id_eafit = models.BigIntegerField(primary_key=True)
    email = models.EmailField()
    passed_workshop = models.BooleanField()
    went_mentorship = models.BooleanField()
    group = models.ForeignKey(Group,blank=True,on_delete=models.SET_NULL)


class Teacher:
     
    name = models.CharField()
    id_eafit = models.BigIntegerField(primary_key=True)
    email = models.EmailField()

class Mentor:

    id_eafit = models.BigIntegerField(primary_key=True)
    name = models.CharField()

class Midterm:
    numTerm = models.PositiveSmallIntegerField()
    fechaIncio = models.DateTimeField()
    fechaFin = models.DateTimeField()

class supMidterm:

    fechaIncio = models.DateTimeField()
    fechaFin = models.DateTimeField()
    parcial = models.ForeignKey(Midterm,on_delete=models.CASCADE,unique=True)










