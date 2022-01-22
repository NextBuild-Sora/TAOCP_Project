
## Django 5.3 超级管理员用户


from django.shortcuts import render
from person_53.models import PersonModel


def show(request):
    persons = PersonModel.objects.all()
    return render( request, "show_53.html", locals() )






