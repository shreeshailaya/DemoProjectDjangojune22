from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from utility.models import Products

# Create your views here.
def index(request):
    return render(request, 'index.html')
