from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse('Welcome to the Polls App.')

# Create your views here.
