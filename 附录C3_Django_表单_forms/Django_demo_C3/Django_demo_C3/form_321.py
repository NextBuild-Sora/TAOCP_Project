
#3.2.1 表单 radio


from django import forms
from django.forms.widgets import RadioSelect


class LoginForm(forms.Form):
    # 第一种方法：
    # scclassA = forms.ChoiceField(label= "班级A", choices= [["21-3-1","21软件-3-1班"], \
    # ["21-3-3", "21软件3-3班"]], initial= "21-3-3")

    # scclassB = forms.ChoiceField(label= "班级B", choices= [["21-3-15","21软件-3-15班"],\
    #     ["32-3-25", "32软件3-25班"]], widget= RadioSelect, initial= "32-3-25")

    # 第二种方法，自定义高：
    CLASS_CHOICES = [["21-3-1","21软件-3-1班"], ["31-3-3", "31软件3-3班"], ["33-3-6", "33软件-3-6班"]]
    scclassA = forms.ChoiceField(label= "班级A", choices= CLASS_CHOICES, initial= "31-3-3")

    scclassB = forms.ChoiceField(label= "班级B", choices= CLASS_CHOICES, widget= RadioSelect, initial= "31-3-3")



