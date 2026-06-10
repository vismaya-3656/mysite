from django.shortcuts import render

def home(request):
    return render(request, 'company_home.html')

def about(request):
    return render(request, 'company_about.html')

def contact(request):
    return render(request, 'company_contact.html')