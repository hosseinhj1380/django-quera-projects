from django.http import HttpResponse
from django.db.models import *
from .models import Book
from .render import render_to_readable_output


def book_list(request):
    min_price = request.GET.get('min_price') or ''
    # Other query parameters
    max_price =  request.GET.get('max_price') or ''
    author = request.GET.get('author') or '' 
    name = request.GET.get('name') or  ''
    all_books=Book.objects.filter(price__gte=min_price,price__lte=max_price,name__contains=name,author__contains=author)
    rendered_string = render_to_readable_output(all_books)
    return HttpResponse(rendered_string)    

   