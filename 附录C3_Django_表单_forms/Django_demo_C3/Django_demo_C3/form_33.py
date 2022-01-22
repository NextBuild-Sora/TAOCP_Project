
#3.3 表单 checkbox


from django import forms
# from django.forms.widgets import RadioSelect


class LoginForm(forms.Form):
    python = forms.BooleanField(label= "python", initial= True, required= False)
    php = forms.BooleanField(label= "php", initial= False, required= False)
    




