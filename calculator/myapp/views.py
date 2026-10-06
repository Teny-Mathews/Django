

from django.shortcuts import render
from django.views import View

class Home(View):
    def get(self, request):
        return render(request, "Home.html")

class Add(View):
    def get(self, request):
        return render(request, "Add.html")
    
    def post(self, request):
        data = request.POST
        n1 = int(data["number1"])
        n2 = int(data["number2"])
        result = n1 + n2
        
        return render(request, "Add.html", {'result': result})