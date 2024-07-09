from django.urls import path
from app1.views import home1,home2

urlpatterns = [
    path('home1', home1, name='home1'),
    path('home2',home2,name='home2')
]