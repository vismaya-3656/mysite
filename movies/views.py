from django.shortcuts import render
from .forms import MovieForm

def movie_form(request):
    message = None

    if request.method == 'POST':
        form = MovieForm(request.POST)

        if form.is_valid():
            movie = form.save()
            message = f"Movie saved: {movie.name} ({movie.year})"
    else:
        form = MovieForm()

    return render(request, 'movie_form.html', {
        'form': form,
        'message': message
    })