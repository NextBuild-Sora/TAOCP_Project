
#3.4 表单 select


from django import forms


class LoginForm(forms.Form):
    COURSELIST = [["python", "Python Course"], ["php", "PHP Corese"], ["WEB", "Web Course"]]
    # courses = forms.MultipleChoiceField(label= "courses", choices= COURSELIST, widget= forms.CheckboxSelectMultiple)   #多选
    courses = forms.MultipleChoiceField(label= "courses", choices= COURSELIST)   #多选







