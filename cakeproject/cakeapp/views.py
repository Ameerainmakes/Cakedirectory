from django.shortcuts import render
from django.http import HttpResponse
from . models import Clients


# Create your views here.
def demo(request):
    obj = Clients.objects.all()
    return render(request, 'index.html', {'result': obj})
