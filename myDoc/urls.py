
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^http://bookadoctor.cloudapp.net/admin/', include(admin.site.urls)),
    url(r'^http://bookadoctor.cloudapp.net/doctors/', include('doctors.urls', namespace='doctors')),
    url(r'^http://bookadoctor.cloudapp.net/search/$', 'doctors.views.search'),
    url(r'^http://bookadoctor.cloudapp.net/booking/(?P<doctor_id>\d+)/$', 'doctors.views.booking_form'),
    url(r'^http://bookadoctor.cloudapp.net/bookingsucced/(?P<doctor_id>\d+)/$', 'doctors.views.booking'),
]
