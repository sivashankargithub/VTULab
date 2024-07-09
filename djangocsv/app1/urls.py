from django.urls import path
from app1.views import home,export_to_csv

urlpatterns = [
    path('', home, name='home'),
    path('csv/',export_to_csv,name='home2'),
]