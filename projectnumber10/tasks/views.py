from django.views.decorators.csrf import csrf_exempt
from .models import Task
from django.http import HttpResponse
# Other required imports here


@csrf_exempt
def list_create_tasks(request):
    if request.method == 'POST':
        task1=request.POST.get('task')
        
        Task.objects.create(name=task1)
        
        return HttpResponse(f"Task Created: '{task1}'")
