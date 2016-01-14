from doctors.models import *
# abstract base classes (abc) , metaclass: ABCMeta
from abc import ABCMeta, abstractmethod
from django.shortcuts import get_object_or_404

class BaseDAO(object):
	print('BaseDAO')

	__metaclass__ = ABCMeta

	@abstractmethod
	def delete(self):
		if (isinstance(self.__localObject__, self.__entityClass__)):
			self.__localObject__.delete()

		return

	@abstractmethod
	def getAll(self):
		self.__localObject__ = self.__entityClass__.objects.all()
		return self.__localObject__

	@abstractmethod
	def getById(self, ID):
		print('BaseDAO')
		self.__localObject__ = get_object_or_404(self.__entityClass__, pk=ID)
		return self.__localObject__


	@abstractmethod
	def save(self):
		if (isinstance(self.__localObject__, self.__entityClass__)):
			self.__localObject__.save()
		return

class PatientDAO(BaseDAO):
	print('PatientDAO')

	__entityClass__ = Patient
	__localObject__ = object()

	def create(self, name):
		self.__localObject__ = self.__entityClass__(name=name)
		return

	def delete(self):
		pass

	def getAll(self):
		pass

	def getById(self, ID):
		pass

	def save(self):
		pass

class DoctorDAO(BaseDAO):
	print('DoctorDAO')

	__entityClass__ = Doctor 
	__localObject__ = object()

	def getByCriteria(self, spec, zipcode):
		self.__localObject__ = self.__entityClass__.objects.filter(specialization=spec, zip_code=zipcode)
		return self.__localObject__

	def getByFilter(self, gen):
		self.__localObject__ = self.__entityClass__.objects.filter(gender=gen)
		return self.__localObject__

	def create(self, name, spec):
		self.__localObject__ = self.__entityClass__(name=name, specialization=spec)
		return

class SpecializationDAO(BaseDAO):
	print('SpecializationDAO')

	__entityClass__ = Specialization
	__localObject__ = object()

	def getByDoctor(self, doctor):
		print("SpecializationDAO")
		self.__localObject__ = self.__entityClass__.objects.filter(doctor = doctor)[0]
		return self.__localObject__

class HospitalDAO(BaseDAO):
	print('HospitalDAO')

	__entityClass__ = Hospital
	__localObject__ = object()

	def getByDoctor(self, doctor):
		print('HospitalDAO')
		self.__localObject__ = self.__entityClass__.objects.filter(doctor = doctor)[0]
		return self.__localObject__

class AppointmentDAO(BaseDAO):
	print('AppointmentDAO')

	__entityClass__ = Appointment
	__localObject__ = object()

	def getByPatient(self, patient):
		listOfAppointments = self.__entityClass__.objects.filter(patient=patient)
		return listOfAppointments
	
	def getByDoctor(self, doctor):
		listOfAppointments = self.__entityClass__.objects.filter(doctor=doctor)
		return listOfAppointments

	def getByID(self, ID):
		listOfAppointments = self.__entityClass__.objects.filter(pk=ID)
		return listOfAppointments


	def getTakenDays(self, doctor, date):
		print('getTakenDays')
		apps = self.__entityClass__.objects.filter(doctor = doctor, date__gt= date)
		days = []

		for item in apps:
			days.append(item.date.day)

		return days

	def create(self, patient, doctor, date, valid):
		self.__localObject__ = self.__entityClass__(patient=patient, doctor=doctor, date=date, validate=valid)
		return
		
class AuthentificationDAO(object):
	def findUserByUsername(self, user, password):
		userFound = Patient.objects.filter(name=user, password=password)
		return userFound
						
