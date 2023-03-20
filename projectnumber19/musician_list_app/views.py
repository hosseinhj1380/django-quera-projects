from django.shortcuts import render, HttpResponse
from .models import Musician, Album
from django.views import View
import json

class Musician_list(View):
    def get (self,request):
        data=''
        musician_name=Musician.objects.values_list('name',flat=True).order_by('name')
        return HttpResponse (f"{''.join(map(str,musician_name))}")
        