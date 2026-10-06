from django.urls import path
from .views import First,Movie_list,Add_movie

urlpatterns = [
    path('first/', First.as_view(), name='first_page'),
    path('movie/', Movie_list.as_view(), name='movie'),
    path('addmovie/', Add_movie.as_view(), name='addmovie'),

]