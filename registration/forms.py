from django import forms

class RegistrationForm(forms.Form):
    full_name = forms.CharField(
        min_length=5,
        max_length=50,
        required=True
    )

    email = forms.EmailField(
        required=True
    )

    password = forms.CharField(
        min_length=8,
        max_length=20,
        widget=forms.PasswordInput,
        required=True
    )