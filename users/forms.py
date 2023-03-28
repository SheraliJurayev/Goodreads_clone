from django import forms


class UserCreateForm(forms.Form):
    username = forms.CharField(max_length=200)
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    email = forms.EmailField()
    password = forms.CharField(max_length=128)
