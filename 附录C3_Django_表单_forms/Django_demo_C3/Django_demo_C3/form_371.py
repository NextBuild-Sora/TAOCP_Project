
# 3.7.1 表单 综合实训


from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import re



class UserForm(forms.Form):
    SEX = [["M","男", ["F", "女"]]]
    user = forms.CharField(label= "用户名称", required= True, max_length= 8)
    pwd = forms.CharField(label= "密码", required= True, widget= forms.PasswordInput, max_length= 8 )
    con_pwd = forms.CharField(label= "确认密码", required= True, widget= forms.PasswordInput, max_length= 8)
    tel = forms.CharField(label= "电话", required= False, max_length= 11 )   #变化框；验证（手机号码的）
    email = forms.EmailField(label= "邮箱", required= False, max_length= 64 ) 

     




    







