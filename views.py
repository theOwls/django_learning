from django.http import HttpResponse

def index(request):
	return HttpResponse("My name is Liam, I like code.")

# Create your views here.
