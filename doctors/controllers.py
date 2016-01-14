from django.shortcuts import get_object_or_404
from doctors.dao import *

class PatientController(object):
	print('PatientController')

	__patientDAO__ = PatientDAO()
	__appointmnentDAO__ = AppointmentDAO()
	__patient__ = object()

	def createAppointment(self, doctor, date, patient):
		self.__appointmnentDAO__.create(null, patient, doctor, date, False)
		return 


class SpecializationController(object):
	print('SpecializationController')
	__specializationDAO__ = SpecializationDAO()

	def getAll(self):
		return self.__specializationDAO__.getAll()

	def getById(self, ID):
		print('SpecializationController')
		return self.__specializationDAO__.getById(ID)

class HospitalController(object):
	print('HospitalController')

	__hospitalDAO__ = HospitalDAO()

	def getAll(self):
		return self.__hospitalDAO__.getAll()

	def getById(self, ID):
		print('HospitalController')

		return self.__hospitalDAO__.getById(ID)
		
		

class DoctorController(object):
	print('DoctorController')

	__doctorDAO__ = DoctorDAO()
	__specializationDAO__ = SpecializationDAO()

	def getById(self, doc_id):
		return self.__doctorDAO__.getById(doc_id)

	def getBySpecHospId(self, spec_id, hosp_id):
		print('DoctorController')
		return self.__doctorDAO__.getByCriteria(SpecializationController().getById(spec_id), HospitalController().getById(hosp_id)) 
		#self.__doctorDAO__.getById(HospitalController().getById(hosp_id))
		

class AppointmentController(object):
	print('AppointmentController')

	__appointmentDAO__ = AppointmentDAO()

	def getTakenDays(self, doctor, date):
		return self.__appointmentDAO__.getTakenDays(doctor, date)
	
	
		
