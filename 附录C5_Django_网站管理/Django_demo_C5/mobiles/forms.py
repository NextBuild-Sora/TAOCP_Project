
#Django 5.4 网站 综合实训


from django import forms


class ProductForm(forms.Form):
    model = forms.CharField(max_length= 128, required= True, label= "型号")
    maker = forms.CharField(max_length= 128, required= True, label= "厂商" )
    year = forms.IntegerField(required = True , label= "年份")
    price = forms.IntegerField(initial= 0, label= "价格")
    qty = forms.IntegerField(initial= 1, label= "数量")
    desp = forms.CharField(max_length= 128, required= False, label= "简介")

class LoginForm(forms.Form):
    name = forms.CharField(max_length= 128, required= True, label= "用户")
    password = forms.CharField(max_length= 128, required= True, label="密码", widget= forms.PasswordInput)





