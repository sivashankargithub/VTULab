from django.shortcuts import render
from app1.forms import Inputform1, Inputform2, Inputform3
from app1.models import Students, Course

def student(request):
    if request.method=="POST":
        form1=Inputform1(request.POST)
        if form1.is_valid():
            form1.save()
            return render(request,'app1/student.html',{'form':form1,'param1':"Success"})
    else:
        form1=Inputform1()
    return render(request,'app1/student.html',{'form':form1})

def course(request):
    if request.method=="POST":
        form1=Inputform2(request.POST)
        if form1.is_valid():
            form1.save()
            return render(request,'app1/course.html',{'form':form1,'param1':"Success"})
    else:
        form1=Inputform2()
    return render(request,'app1/course.html',{'form':form1})

def filter1(request):
    if request.method=="POST":
        form1=Inputform3(request.POST)
        if form1.is_valid():
            data=form1.cleaned_data
            in1=data.get('input1')
            cname=Course.objects.get(course=in1)
            print(cname.id)
            temp = Students.objects.filter(course=cname.id)
            result=dict(temp.values_list())
            return render(request,'app1/filter1.html',{'form':form1,'param1':result})
    else:
        form1=Inputform3()
    return render(request,'app1/filter1.html',{'form':form1})