from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Rand
import requests

def index(request):
    req = request.GET['grupa']
    randuri = Rand.objects.filter(grupa = req)
    template = loader.get_template('index.html')
    context = {'randuri': randuri, 'grupa': req }

    return HttpResponse(template.render(context,request))