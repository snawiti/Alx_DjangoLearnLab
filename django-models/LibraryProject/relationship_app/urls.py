from django.urls import path
from django.http import HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    list_books,
    LibraryDetailView,
    login_view,
    logout_view,
    register_view,
)

def home(request):
    return HttpResponse("<h1>Welcome</h1>")

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('', home, name='home'),
]

