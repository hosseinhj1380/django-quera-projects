from .models import Book
from django.shortcuts import render


def booklist(request):
    book=Book.objects.all()
    context1={'books':book}
    return render(request,'booklist.html',context=context1)
