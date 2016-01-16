from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /doctors/
    url(r'^http://bookadoctor.cloudapp.net/$', views.home, name='home'),
    url(r'^http://bookadoctor.cloudapp.net/(?P<doctor_id>[0-9]+)/$', views.showDoctorDetails, name='detail'),
]
