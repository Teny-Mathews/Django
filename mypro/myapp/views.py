from django.shortcuts import render
from django.views import View
from myapp.models import Person


class First(View):
    def get(self,request):

        # data=[{"name":"Arun","age":21,"place":"Ekm"},
        #       {"name":"Arun V","age":26,"place":"Ktm"},
        #       {"name":"Arun D","age":24,"place":"Idk"}]

        data=Person.objects.all()
        
        context = {"data": data} 
        return render(request, "First.html", context)

from myapp.models import Movie
class Movie_list(View):
    def get(self,request):
        m=Movie.objects.all()
        print(m)
        context={"movies":m}
        return render(request,"Movie_list.html",context)

class Add_movie(View):
    def get(self,request):
        return render(request,"Add_movie.html")

    def post(self,request):
        print(request.POST)

        data=request.POST
        n=data['name']
        d=data['director']
        y=data['year']
        print(n,d,y)

        m=Movie.objects.create(name=n,director=d,year=y)
        m.save()
        return render(request,"Add_movie.html")

    
