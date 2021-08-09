from django.shortcuts import render, HttpResponse
from time import gmtime, strftime
from django.utils import timezone
    
def index(request):
    context = {
        "time": strftime("%d-%m-%Y %H:%M %p", gmtime()),
        "h1rojo": "h1{color:red;}",
        "h2azul": "h2{color:blue;}"
    }

    return render(request,'time_display/index.html',context)