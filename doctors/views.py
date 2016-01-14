from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string

from doctors.controllers import *
from doctors.forms import *

specControl = SpecializationController()
docControl = DoctorController()
appControl = AppointmentController()


def home(request):
	specializationList = specControl.getAll()
	context = {'specializationList': specializationList}
	return render(request, 'doctors/searchForm.html', context)

def search(request):
	if request.method=='GET':
		form=SearchDoc(request.GET)
		if form.is_valid():
			specialization = form.cleaned_data['specialization']
			zip_code = form.cleaned_data['zip_code']

			spec_id = (Specialization.objects.get(type=specialization)).id
			hosp_id = (Hospital.objects.get(zip_code=zip_code)).id

			doctors = docControl.getBySpecHospId(spec_id, hosp_id)
			return render(request, 'doctors/doctorlist.html', 
			{'doctors': doctors })
	
def booking_form(request, doctor_id):

	doctor = docControl.getById(doctor_id)

	return render(request, 'doctors/bookingForm.html', {"doctor" : doctor})


def booking(request, doctor_id):
	if request.method == 'POST':
		form = BookDoc(request.POST)
		print(form)
		if form.is_valid():
			print('is_valid')
			firstName = form.cleaned_data['firstName']
			lastName = form.cleaned_data['lastName']
			phone = form.cleaned_data['phone']
			email = form.cleaned_data['email']

			doctor = docControl.getById(doctor_id)

			#data = {'firstName': firstName, 
			#		'lastName'  : lastName}
			#template = 'doctors/email_new.html'
			#msg      = render_to_string(template,  data)

			#send_mail(('New booking | MyDocc'), msg, 'myDoc@example.com', [email], fail_silently=False)
            
			return HttpResponse('Check your email for confirmation code')

	else:
		form = BookDoc()

		return render(request, 'doctors/bookingForm.html', {'form' : form})

def showDoctorDetails(request, doctor_id):
	try: 
		doctor = docControl.getById(doctor_id)

		year = timezone.now().year
		month = timezone.now().month
		day = timezone.now().day

		available_days = []
		taken_days = appControl.getTakenDays(doctor, timezone.now())

		for day in range(day, day + 3):
			if (day not in taken_days):
				available_days.append(day)
		print(available_days)

	except Doctor.DoesNotExist:
		raise Http404('Doctor does not exist')
	return render(request, 'doctors/doctordetail.html', {'doctor' : doctor, 'available_days': available_days, 'year': year, 'month': month})

