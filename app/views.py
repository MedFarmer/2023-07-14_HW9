from django.shortcuts import render, redirect
from .models import Hotel
from random import randint

def index(request):
    hotels = Hotel.objects.all()
    context = {'hotels':hotels}
    return render(request, 'index.html', context)

def add_hotel(request):    
    if request.method == "POST": 
        hotels = request.POST                    
        name = hotels['name']            
        add = Hotel()
        add.name = name            
        add.save()
        return redirect('index')     
    else:
        choices = ["Marriot","Rixos","Sheraton","St Regis","Radison","Ritz"]
        context = {'choices': choices}
        return render(request, 'add_hotel.html', context)

def delete(request):
    hotels = Hotel.objects.all()
    # context = {'hotels':hotels}
    hotels.delete()
    return redirect('index')

def cyclical_add_hotel(request):
    if request.method == 'POST':
        choices = ["Marriot","Rixos","Sheraton","St Regis","Radison","Ritz"]                 
        for i in range(0,len(choices)):     
            name = choices[randint(0, len(choices)-1)]       
            add = Hotel()
            add.name = name    
            add.save()
        return redirect('index')
    else:
        return render(request, 'cyclical_add_hotel.html')