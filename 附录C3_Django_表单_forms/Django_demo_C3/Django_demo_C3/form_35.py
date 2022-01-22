
#3.5 表单 textarea
#多行表单


from django import forms


class LoginForm(forms.Form):
    note = forms.CharField(label= "Note", widget= forms.Textarea(attrs={"style":"width:600px;height:300px"}))   #多行文本.







