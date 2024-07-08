from django.shortcuts import render
def home(request):
    list1=['Aditya','Balu','Chandru', 'Rajesh','Shasahank', 'Ramachandra','Sivappa']
    return render(request,'app1/index.html',{'param1':list1})