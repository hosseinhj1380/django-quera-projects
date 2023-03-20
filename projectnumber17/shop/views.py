from django.http import HttpResponse,HttpResponseBadRequest
from django.shortcuts import render

from .forms import PersonalInformation
from .models import Person


def show_people(request):
    if request.method == 'GET':
        persons = Person.objects.all()
        context = {
            'persons': persons
        }
        return render(request, 'show_people.html', context)


def submit_person(request):
    if request.method == 'GET':
        form=PersonalInformation(request.GET)
        return render ( request, 'new_person.html' , {'form':form}) 
        
    elif request.method == 'POST':
        form=PersonalInformation(request.POST)
        if form.is_valid():
            persons=Person()
            persons.gender=form.cleaned_data["gender"]
            persons.full_name=form.cleaned_data['full_name']
            persons.height=form.cleaned_data['height']
            persons.age=form.cleaned_data['age']
            persons.save()
            return HttpResponse (persons, status=201  )  
          
        return HttpResponseBadRequest('Error',status=400)      
