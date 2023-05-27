from django.db import models

# Create your models here.







class Teacher(models.Model):
     
    name = models.CharField(max_length=100)
    id_eafit = models.BigIntegerField(primary_key=True)
    email = models.EmailField()

class Mentor(models.Model):

    id_eafit = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)

class Midterm(models.Model):
    numTerm = models.PositiveSmallIntegerField()
    fechaIncio = models.DateTimeField()
    fechaFin = models.DateTimeField()

class supMidterm(models.Model):

    fechaIncio = models.DateTimeField()
    fechaFin = models.DateTimeField()
    parcial = models.OneToOneField(Midterm,on_delete=models.CASCADE)

class Group(models.Model):

     id = models.BigIntegerField(primary_key=True)
     enabled_sup = models.OneToOneField(supMidterm,null=True,on_delete=models.CASCADE)
     teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)

class Student(models.Model):

    name = models.CharField(max_length=100)
    id_eafit = models.BigIntegerField(primary_key=True)
    email = models.EmailField()
    passed_workshop = models.BooleanField()
    went_mentorship = models.BooleanField()
    group = models.ForeignKey(Group,blank=True,on_delete=models.CASCADE)








