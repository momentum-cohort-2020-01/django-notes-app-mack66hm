from django.shortcuts import render
from django.http import HttpResponse

import data 

# Create your views here.
def index(request):
    # return HttpResponse("Hello, lets get started.")
    notes = data.NOTES
    return render(request, 'base.html', {'notes': notes})