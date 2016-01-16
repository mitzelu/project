
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^doctors/', include('doctors.urls', namespace='doctors')),
    url(r'^search/$', 'doctors.views.search'),
    url(r'^booking/(?P<doctor_id>\d+)/$', 'doctors.views.booking_form'),
    url(r'^bookingsucced/(?P<doctor_id>\d+)/$', 'doctors.views.booking'),
]
