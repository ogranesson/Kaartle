from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    template_name = 'test.html'
    return render(request, template_name)