import datetime

from django.db import models
from django.contrib.auth.models import (AbstractBaseUser)
from django.utils import timezone
from doctors.managers import *

# Create your models here.
class Specialization(models.Model):
	type = models.CharField(max_length=30)

	def __str__(self):
		return self.type

class Hospital(models.Model):
	zip_code = models.CharField(max_length=7)
	address  = models.CharField(max_length=50)
	name     = models.CharField(max_length=30)

	def __str__(self):
		return self.zip_code

class Doctor(AbstractBaseUser):
	name = models.CharField(max_length=50)
	specialization = models.ForeignKey(Specialization)
	#avaiable_date = models.DateTimeField('date free')
	zip_code = models.ForeignKey(Hospital)
	photo = models.ImageField(default = 'image')
	rating = models.CharField(max_length=50)
	gender = models.CharField(max_length=10)
	education = models.TextField(default = 'education')

	objects = DoctorManager()

	def get_name(self):
		return self.name


	def __str__(self):
		return self.name
		

class Patient(AbstractBaseUser):
	name = models.CharField(max_length=100)
	date_of_birth = models.CharField(max_length=25)
	symptoms = models.TextField()

	objects = PatientManager()

	def get_name(self):
		return self.name

	def __str__(self):
		return self.name


class Appointment(models.Model):
	patient = models.ForeignKey(Patient)
	doctor = models.ForeignKey(Doctor)
	date   = models.DateTimeField('created at:', default=timezone.now())
	validate = models.BooleanField(default=False)

	def __str__(self):           
		buffer = "date: " + str(self.date)
		return str(buffer)
		