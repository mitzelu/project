from django.contrib import admin

# Register your models here.

from .models import *

class DoctorAdmin(admin.ModelAdmin):
	
	list_display = ('name', 'specialty')

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Specialization)
admin.site.register(Hospital)