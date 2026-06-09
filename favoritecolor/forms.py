from django import forms

class FavoriteColorForm(forms.Form):
    name = forms.CharField(
        label="Name",
        required=True
    )

    color = forms.CharField(
        label="Favorite Color",
        required=True
    )