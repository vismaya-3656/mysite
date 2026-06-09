from django.shortcuts import render
from .forms import FavoriteColorForm

def favorite_color(request):
    if request.method == "POST":
        form = FavoriteColorForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            color = form.cleaned_data["color"]

            return render(request, "color_result.html", {
                "name": name,
                "color": color,
                "form_data": request.POST
            })

    else:
        form = FavoriteColorForm()

    return render(request, "form.html", {
        "form": form
    })