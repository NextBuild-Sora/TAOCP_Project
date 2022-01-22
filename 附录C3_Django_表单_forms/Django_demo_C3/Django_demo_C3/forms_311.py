
# 3.1.1 表单 text password


from django import forms


class BookForm(forms.Form):  #forms.Form是系统的表单类
    #CharField是文本输入框
    ISBN = forms.CharField(label= "ISBM", required= True)
    Name = forms.CharField(label= "书名", required= True)
    Author = forms.CharField(label= "作者", required= False)
    Price = forms.DecimalField(label="价格")


    
