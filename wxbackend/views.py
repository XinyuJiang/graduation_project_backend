from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.

@csrf_exempt
def index(request):
    return HttpResponse("Hello, world. You're at the DGD index.")
