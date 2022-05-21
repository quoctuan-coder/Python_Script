import imp
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> respone
# request handler
# action

def say_hello(request):
    # Pull ata from db
    # return HttpResponse('Hello world')

    # using template
    x = 1
    y = 2
    
    return render(request,'hello.html',{'name':'Mosh'})

