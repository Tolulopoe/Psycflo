from django.http import HttpResponse
from django.template import loader
from .models import Aid

# Create your views here.
def AidObjects(request):
    aids = Aid.objects.all().values()  # Fetch all Aid objects
    template = loader.get_template('Aidobjects.html')
    context = {
        'aids': aids,  # Pass the actual queryset, not the string 'aids'
    }
    return HttpResponse(template.render(context, request))
