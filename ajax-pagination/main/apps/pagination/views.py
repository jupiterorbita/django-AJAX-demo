from django.shortcuts import render, HttpResponse, redirect
from .models import *
import datetime


def index(request):
    print('\ninside index <=-=-=-=-=-=')
    # leads = Lead.objects.all()
    leads = Lead.objects.order_by('first_name')
    return render(request, 'pagination/index.html', {'leads': leads})


def name_search(request):
    print('\ninside name_search <===')
    # leads = Lead.objects.filter(first_name__startswith=request.POST['name']) | Lead.objects.filter(last_name__startswith=request.POST['name'])
    leads = Lead.objects.filter(first_name__contains=request.POST['name']) | Lead.objects.filter(last_name__contains=request.POST['name'])
    return render(request, 'pagination/show.html', {'leads': leads})


# demo date get from POST
def date_get(request):
    date_entered = request.POST.get('date')
    print('date ==>', date_entered)
    return redirect('/')


# if the day len is empty pass back an empty array
def get_day(request):
    if len(request.POST['day_num']) <1:
        return render(request, 'pagination/show.html', {'leads': []})
    else:
        leads = Lead.objects.filter(created_at__day=request.POST['day_num'])
        return render(request, 'pagination/show.html', {'leads': leads})
