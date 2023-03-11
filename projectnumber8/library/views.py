from django.http import HttpResponse
from django.db.models import *
from .models import Book
from .render import render_to_readable_output

# what is diffrent between result in these function
# def book_list(request):
#     min_price = request.GET.get('min_price') or ''
#     # Other query parameters
#     max_price =  request.GET.get('max_price') or ''
#     author = request.GET.get('author') or '' 
#     name = request.GET.get('name') or  ''
    
# def book_list(request):
#     min_price = request.GET.get('min_price','')  
#     # Other query parameters
#     max_price =  request.GET.get('max_price','') 
#     author = request.GET.get('author','') 
#     name = request.GET.get('name','') 


    all_books=Book.objects.filter(price__gte=min_price,price__lte=max_price,name__contains=name,author__contains=author)
    rendered_string = render_to_readable_output(all_books)
    return HttpResponse(rendered_string)    

    # if rendered_string is None:
    #     all_books=Book.objects.all()
    # else :
    #     return HttpResponse(rendered_string)    


