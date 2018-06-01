from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
from django.core import serializers


def index(request):
    return render(request, 'djangoajaxnotes/index.html')

def add(request):
    if request.method == 'POST':
        Note.objects.create(actual_note=request.POST['note_here'])
        notes=Note.objects.order_by('-id')
        return render(request, 'djangoajaxnotes/add.html', {'notes':notes})
    else:
        return redirect('/')

def reset(request):
    Note.objects.all().delete()
    return redirect('/')
