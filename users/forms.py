from django import forms

from .models import User


class LoginForm(forms.Form):

    email = forms.EmailField(max_length=255)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)


class RegisterForm(forms.Form):

    email = forms.EmailField(max_length=255)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)
    password_repeat = forms.CharField(max_length=255, widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    city = forms.CharField(max_length=255)
    country = forms.CharField(max_length=255)
    zip_code = forms.CharField(max_length=6)
    street_address = forms.CharField(max_length=255)
    bank_name = forms.CharField(max_length=255)
    iban = forms.CharField(max_length=255)
    bic = forms.CharField(max_length=255)
    phone_number = forms.CharField(max_length=255)
    ust_idnr = forms.CharField(max_length=100)
    nip = forms.CharField(max_length=10)

    def clean(self) -> dict:

        if self.cleaned_data['password'] != self.cleaned_data['password_repeat']:
            raise forms.ValidationError("Passwords do not match.")

        return self.cleaned_data
