
#3.6 表单 数据验证
#表单提交


from django import forms
from django.core.validators import RegexValidator
import re



class LoginForm(forms.Form):
    name = forms.CharField( label= "Name", required= True )   
    sex = forms.CharField( label= "Sex", max_length= 1, validators= [RegexValidator(r"[M,F]", "性别必须是M 或者F ")] )
    age = forms.CharField( label= "Age", max_length= 2, validators= [RegexValidator(r"\d{2}", "年龄必须是2位数")] )








