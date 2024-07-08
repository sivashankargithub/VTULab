from django.shortcuts import render
def home(request):
    list1=['Apple','Banana','Black Berry','Orange','Pine Apple']
    return render(request,'app2/index.html',{'param1':list1})