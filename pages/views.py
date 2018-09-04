from django.shortcuts import render , HttpResponse


# Create your views here.
def page(request):
    return HttpResponse('Test URLs')
