from django.urls import path
from .views import Add,Home

urlpatterns = [
    path('home/', Home.as_view(), name='Home'),
    path('add/', Add.as_view(), name='Add'),
]