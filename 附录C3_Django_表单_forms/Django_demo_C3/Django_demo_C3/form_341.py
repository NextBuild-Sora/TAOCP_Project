
#3.4.1 表单 select


from django import forms


class UserForm(forms.Form):
    ClassList = [["21-3-2", "21软件-3-2班"], ["21-3-22", "21软件-3-22班"], ["21-3-23", "21软件-3-23班"], ["21-3-24", "21软件-3-24班"], ]
    # sclass = forms.ChoiceField(label= "班级", choices= ClassList)

    sclass = forms.MultipleChoiceField(label= "班级", choices= ClassList, required= False)   #多选






