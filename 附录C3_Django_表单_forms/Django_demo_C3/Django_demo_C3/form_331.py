
#3.3.1 表单 checkbox


from django import forms
# from django.forms.widgets import RadioSelect


class LoginForm(forms.Form):
    COURSELIST = [["python", "Python Course"], ["php", "PHP Corese"],["Web", "Web Course"]]
    courses = forms.MultipleChoiceField(label= "courses", choices= COURSELIST, widget= forms.CheckboxSelectMultiple)   #多选
    # courses = forms.MultipleChoiceField(label= "courses", choices= COURSELIST)   #多选







