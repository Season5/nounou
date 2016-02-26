from django.http import HttpResponse

def index(request):
    return HttpResponse("She says hey there world!")