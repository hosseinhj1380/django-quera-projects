from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.http import HttpResponse

@csrf_exempt
def delete_task(request, task_id):
    if request.method == 'DELETE':
        try:
            name=Task.objects.get(id=task_id).name
            Task.objects.get(id=task_id).delete()
            
            return HttpResponse (f"Task Done: '{name}'")
        except:
            return HttpResponse (f"There isn't any task with id '{task_id}'")
