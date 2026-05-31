from django.shortcuts import render

def employee_directory(request):
    employees = [
        {
            'name': 'Manu',
            'job_title': 'Software Engineer',
            'salary': 60000,
            'is_full_time': True
        },
        {
            'name': 'Amal',
            'job_title': 'Designer',
            'salary': 35000,
            'is_full_time': False
        },
        {
            'name': 'Arjun',
            'job_title': 'Manager',
            'salary': 80000,
            'is_full_time': True
        }
    ]

    return render(request, 'employee_directory.html', {
        'employees': employees
    })