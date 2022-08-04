from unicodedata import name
from django.shortcuts import render
#importing loading from django template  
from django.template import loader  
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('Hello Martin!!')
def first(request):
    return HttpResponse('Hello World from First_App')
def index(request):  
   template = loader.get_template('index.html') # getting our template
   name = { 'student':'chakradhar'}  
   return HttpResponse(template.render(name))       # rendering the template in HttpResponse  


   