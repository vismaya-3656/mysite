from django.shortcuts import render

def home(request):
    return render(request, 'website_home.html')

def about(request):
    return render(request, 'website_about.html')