from django.http import JsonResponse
from django.shortcuts import render
from app1.forms import InputForm

def home1(request):
    form1 = InputForm()
    return render(request,'app1/index.html',{'form':form1})

def home2(request):
    if request.method=="POST":
        form1=InputForm(request.POST)
        if form1.is_valid():
            data=form1.cleaned_data
            in1=data.get('input1')
            result=names(in1)
            return JsonResponse({'param1':result})
    else:
        return JsonResponse()
def names(search1):
    list1=['Shubman','Abhishek','Ruturaj','Sanju','Shivam','Riyan','Rinku','Ravi','Sunder','Mukesh','Avesh']
    temp=list(filter(lambda i:i.startswith(search1),list1))
    return temp