import datetime as dt
from django.shortcuts import render
def home(request):
    time1=dt.datetime.now()
    time2=time1+dt.timedelta(hours=4)
    time3=time1+dt.timedelta(hours=-4)
    return render(request,'app1/index.html',{'param1':time1,'param2':time2,'param3':time3})