from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# Function-based view: List all books
def list_books(request):
    books = Book.objects.all()
    output = "\n".join([f"{book.title} by {book.author.name}" for book in books])
    return HttpResponse(output)

# Class-based view: Display details for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
