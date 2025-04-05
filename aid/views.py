from django.http import HttpResponse
from django.template import loader
'''from django.shortcuts import render'''
from .models import Aid

def Aid_objects(request):
    aids=Aid.objects.all().values()
    template =loader.get_template('Aidobjects.html')
    context={
        'aids':'aids',
    }
    return HttpResponse(template.render(context,request))


# Create your views here.
