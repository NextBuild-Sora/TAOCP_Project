
from django import forms


class LoginForm(forms.Form):
    user = forms.CharField(label= "UserName", required= True, max_length= 8)
    password = forms.CharField(label= "Password", widget= forms.PasswordInput, required= True, max_length= 8)
