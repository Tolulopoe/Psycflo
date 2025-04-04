
from django.http import HttpResponse
from django.template import loader
'''from django.shortcuts import render'''
from .models import Aid
# Create your views here.
def Aid_objects(request):
    aids=Aid.objects.all().values()
    template =loader.get_template('Aidobjects.html')
    context={
        'aids':'aids',
    }
    return HttpResponse(template.render(context,request))


'''from django.http import HttpResponse
from django.template import loader

def testing(request):
  template =loader.get_template('Aidobjects.html')
  context = {
    'brandname': 'Molped',
  }
  return HttpResponse(template.render(context, request)) '''                

# Create your views here.
