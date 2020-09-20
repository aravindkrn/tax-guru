from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def upload(request):
    return render(request, 'home.html', {'error': 'Please upload a valid file !'})