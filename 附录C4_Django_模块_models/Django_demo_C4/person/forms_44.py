
#Django 4.4 模块 综合实训



from django import forms


class PersonInsertForm(forms.Form):
    SEX= [["M", "男"], ["F", "女"]]
    Name = forms.CharField(label= "姓名", max_length= 16, required= True)
    Sex = forms.ChoiceField(label = "性别", choices= SEX, initial="M")
    Age = forms.IntegerField(label= "年龄")
    Tel = forms.CharField(label= "电话")

class PersonUpdateForm(forms.Form):
    SEX = [["M", "男"], ["F", "女"]]
    Sex = forms.ChoiceField(label= "性别", choices= SEX, initial= "M")
    Age = forms.IntegerField(label= '年龄')
    Tel = forms.CharField(label= "电话")
    


    