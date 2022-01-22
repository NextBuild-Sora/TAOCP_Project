
#3.4.2 表单 



from django import forms


class UserForm(forms.Form):
    # sclass = forms.ChoiceField(label= "班级", choices= ClassList) #单选

    sclass = forms.MultipleChoiceField(label= "班级", required= False)   #多选






