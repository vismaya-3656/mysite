from django.shortcuts import render

def user_form(request):
    return render(request, 'user_form.html')

def result(request):
    username = request.GET.get('username')

    context = {
        'username': username,
        'form_data': request.GET
    }

    return render(request, 'result.html', context)