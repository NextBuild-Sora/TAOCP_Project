
# 3.7 表单 综合实训


from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import re


def tel_validate(value):
    tel = re.compile(r'^(13[0-9]|15[0123456789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
    if not tel.match(value):
        raise ValidationError("手机号码格式错误")

class RegisterForm(forms.Form):
    SEX = [["M","男", ["F", "女"]]]
    user = forms.CharField(label= "用户名称", required= True, max_length= 8)
    sex = forms.ChoiceField(label= "性别", choices= SEX, initial= "M")
    age = forms.IntegerField(label= "年龄", validators= [RegexValidator(r"\d{1,2}", "年龄是1-2位数值")])
    pwd = forms.CharField(label= "密码", required= True, widget= forms.PasswordInput(attrs= {"id":"pwd"}) )
    pwdConfirm = forms.CharField(label= "确认密码", required= True, widget= forms.PasswordInput(attrs= {"id":"pwdConfirm"}), max_length= 8)
    tel = forms.CharField(label= "电话", required= False, max_length= 11, validators= [tel_validate] )   #变化框；验证（手机号码的）
    email = forms.EmailField(label= "Email", required= False)



    







