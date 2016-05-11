from django.shortcuts import render
# from django.http import HttpResponse

def landing(request):


    return render(request, 'nounou/landing.html')


def main(request):

	return render(request, 'nounou/main.html')


def reggy(request):

	return render(request, 'nounou/register.html')



