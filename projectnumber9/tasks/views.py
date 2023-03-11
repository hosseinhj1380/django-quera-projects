# Needed imports here
from .models import Task
from django.http import HttpResponse


def list_create_tasks(request):
    if request.method == 'GET':
        task1=Task.objects.order_by('name')
        
        return HttpResponse('\n'.join(map(str,task1)))


def count_tasks(request):
    if request.method == 'GET':
        task1=Task.objects.count()
        return HttpResponse (f"You have '{task1}' tasks to do")
       


