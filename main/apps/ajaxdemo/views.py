from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from .models import *

from django.core import serializers

def index(request):
    return render(request, "ajaxdemo/index.html")

# =========================== DEMO 1 ===============================
def all_json(request):
    users = User.objects.all()
    users_json = serializers.serialize("json", users)
    # print('\n users_json = ', users_json)
    return HttpResponse(users_json, content_type="aplication/json")


def all_html(request):
    users = User.objects.all()
    return render(request, 'ajaxdemo/all.html', {'users': users})


# ========================== DEMO 2 ================================
def find(request):
    print('first name method inside =-=-=-==')
    users = User.objects.filter(first_name__startswith=request.POST['first_name_starts_with'])
    # print('from find method - users =>', users)
    return render(request, 'ajaxdemo/all.html', {'users': users})

def find_last(request):
    print('last name method inside =-=-=-=-=')
    users = User.objects.filter(last_name__startswith=request.POST['last_name_starts_with'])
    print('user_last =>', users)
    return render(request, 'ajaxdemo/all.html', {'users': users})

def find_age(request):
    print('\n server > age method')
    users = User.objects.filter(age__startswith=request.POST['age_starts_with'])
    context = {
        'users': users
    }
    print('user_age filter', users)
    return render(request, 'ajaxdemo/all.html', context)

def create(request):
    print('\n server > create')
    User.objects.create(first_name=request.POST['first_name'],
                        last_name=request.POST['last_name'],
                        email=request.POST['email_address'])
    users = User.objects.order_by('-id')
    # messages.success(request, 'successfully added new user in the db')
    return render(request, 'ajaxdemo/all.html', {'users':users})
    