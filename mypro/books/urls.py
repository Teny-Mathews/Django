from django.urls import path
from .views import Home,Add_book,View_book

urlpatterns = [
    path('home/', Home.as_view(), name='Home'),
    path('addbook/', Add_book.as_view(), name='AddBook'),
    path('viewbook/', View_book.as_view(), name='ViewBook'),
]