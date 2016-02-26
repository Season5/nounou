from django.shortcuts import render
# from django.http import HttpResponse

def index(request):


    return render(request, 'nounou/index.html')


# def main(request):

# 	return render(request, 'nounou/main.html')
