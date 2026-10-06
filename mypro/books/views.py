from django.shortcuts import render
from django.views import View
from books.models import Book

class Home(View):
    def get(self,request):
        return render(request,"Home.html")

class Add_book(View):
    def get(self,request):
        return render(request,"Add_book.html")

    def post(self,request):
        print(request.POST)

        data=request.POST
        t=data['title']
        a=data['author']
        p=data['price']
        l=data['language']
        pg=data['pages']
        print(t,a,p,l,pg)

        m=Book.objects.create(title=t,author=a,price=p,language=l,pages=pg)
        m.save()
        return render(request,"Add_book.html")

class View_book(View):
    def get(self,request):
            b=Book.objects.all()
            print(b)
            context={"books":b}
            return render(request,"View_book.html",context)  