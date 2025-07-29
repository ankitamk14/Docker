from django.http import HttpResponse
from .models import Book

def index(request):
    books_count = Book.objects.count()
    return HttpResponse(f"Hello from demo app! : {books_count}")
