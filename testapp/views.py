from django.shortcuts import render , render_to_response ,HttpResponse
from datetime import date ,datetime
# Create your views here.

def index(request):
    return HttpResponse('Ordinary life 2018')

def home(request):
    return HttpResponse('Welcome back to django 2.1 - {} '.format(compute_age('01091990')))

def parameters(request):
    return HttpResponse('Ordinary life parameters')

def compute_age(dob):
    birth_date = datetime.strptime(dob,"%d%m%Y")
    w_age = date.today().year-birth_date.year -((date.today().month,date.today().day)<(birth_date.month,birth_date.day))
    return w_age
