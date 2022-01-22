
#Django 4.2.1 模块 操作数据


from django import forms

class PersonForm(forms.Form):
    SEXLIST= [["男", "男"], ["女", "女"]]
    Name = forms.CharField(label= "Name", required= True)
    Sex = forms.ChoiceField(label = "Sex", choices= SEXLIST, initial="男")
    Age = forms.IntegerField()


    