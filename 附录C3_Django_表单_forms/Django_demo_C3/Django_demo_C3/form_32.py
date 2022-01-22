
#3.2 表单 radio


from django import forms


class LoginForm(forms.Form):
    SEXLIST = [ ["M", "男"], ["F", "女"] ]
    user = forms.CharField(label= "Name", required= True, max_length= 8)
    sex = forms.ChoiceField(label= "Sex", choices= SEXLIST, initial= "M", widget= forms.RadioSelect)


