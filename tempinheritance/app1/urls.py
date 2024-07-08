from django.urls import path
from app1.views import doctorlayout,doctor1,doctor2,doctor3
urlpatterns = [
    path('doctorlayout/', doctorlayout, name='doctorlayout'),
	path('doctor1/', doctor1, name='doctor1'),
    path('doctor2/', doctor2, name='doctor2'),
    path('doctor3/', doctor3, name='doctor3'),
    ]