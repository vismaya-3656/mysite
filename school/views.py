from django.shortcuts import render

def home(request):
    students = [
        "Arun",
        "Manu",
        "Anu",
        "Rahul"
    ]

    return render(request, 'school_home.html', {
        'students': students
    })


def result(request, name):
    return render(request, 'school_result.html', {
        'name': name
    })