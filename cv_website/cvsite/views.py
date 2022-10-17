from django.shortcuts import render
from .models import cvelement

# Create your views here.

def cvsite(request):
    cvelements = cvelement.objects.all()
    return render(request, 'cvsite/homepage.html', {'cvelements': cvelements})
def contatti(request):
    return render(request, 'cvsite/contatti.html')
def curriculum (request):
    return render(request, 'cvsite/curriculum.html')
    ...

import mimetypes
import os
from django.http.response import HttpResponse

...

def download_file(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		# Modifica filename con il nome e l'estensione del file che vuoi far scaricare	
    filename = 'largepreview.png'
    filepath = BASE_DIR + '/download/' + filename
    path = open(filepath, 'rb')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response


from django.http import Http404
...

def detail(request, cvelement_id):
    try:
        element = cvelement.objects.get(pk=cvelement_id)

    except cvelement.DoesNotExist:
        raise Http404("CV element does not exist")
    return render(request, 'cvsite/detail.html', {'element': element})