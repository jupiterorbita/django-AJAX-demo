from django.http import JsonResponse

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
from django.core import serializers


def index(request):
    notes=Note.objects.order_by('-id')
    return render(request, 'notes/index.html', {'notes':notes})
    # notes=Note.objects.order_by('-id')
    # return render(request, 'notes/index.html', {'notes':notes})


def add(request):
    if request.method == 'POST':
        note = Note.objects.create(actual_note=request.POST['note_here'])
        # notes=Note.objects.order_by('-id')
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print(note) 
        return render(request, 'notes/add.html', {'note': note})
    else:
        return redirect('/')


def reset(request):
    Note.objects.all().delete()
    return redirect('/')


def delete(request, number):
    if request.method == 'POST':
        Note.objects.get(id=number).delete()
        return HttpResponse('cool')