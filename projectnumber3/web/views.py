from django.http import HttpResponse


def sad (request,name ):
    return HttpResponse (f"Nobody likes you, {name}!")

def happy (request,name,times):
    show=''
    for i in range (times):
        show=f"You are great, {name} :)\n"+show
    
    return HttpResponse(show)


