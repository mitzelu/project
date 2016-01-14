from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /doctors/
    url(r'^$', views.home, name='home'),
    url(r'^(?P<doctor_id>[0-9]+)/$', views.showDoctorDetails, name='detail'),
]