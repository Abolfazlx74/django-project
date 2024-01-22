from django.shortcuts import render
import datetime 
from .models import circus
from django.http import HttpResponse
from .forms import InputForm
def my_view(request):
    context = {
        "author": "Gaurav Singhal",
        "website": {
            "views": 200
        },
        "odds": [1, 3, 5]
    }
    
    return render(request, "index.html", context)
# Create your views here.
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>it is now %s</body></html>"%now
    return HttpResponse(html)
def member_form(request):
    context = {}
    context['form'] = InputForm()
    return render(request,"form.html",context)