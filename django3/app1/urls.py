from django.urls import path
from app1.views import student,course,filter1
urlpatterns = [
	path('student/', student),
    path('course/', course),
    path('filterbycourceid/', filter1)
    ]