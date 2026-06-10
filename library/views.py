from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()

    return render(request, 'book_form.html', {'form': form})


def book_list(request):
    books = Book.objects.all()

    return render(request, 'book_list.html', {
        'books': books
    })