from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from myapp.models import Employee

# Create your views here.
from json import loads
import json

class Employeelist(View):
    def get(self,request):
        e=Employee.objects.all().values()
        print(e)
        print(type(e))

        # e=Employee.objects.all()
        # print(e)
        # print(type(e))

        data=list(Employee.objects.all().values())
        print(data)
        print(type(data))

        return JsonResponse(data,safe=False)

    

from json import loads
import json

@method_decorator(csrf_exempt,name="dispatch")

class Employeecreate(View):
    def post(self,request):

        data=loads(request.body)

        r=data["empid"]
        n=data["name"]
        a=data["age"]
        p=data["place"]
        g=data["gender"]
        j=data["joining_date"]
        s=data["salary"]
        d=data["designation"]

        s=Employee.objects.create(**data)
        s.save()

        return JsonResponse({"message":"Inserted Data Successfully"})
    

@method_decorator(csrf_exempt,name="dispatch")
class Employeeretrieve(View):
    
    def get(self,request,i):
        e=list(Employee.objects.filter(id=i).values())
        if e:
            return JsonResponse(e,safe=False)
        else: 
            return JsonResponse({"Message":"No employee Data"})


@method_decorator(csrf_exempt,name="dispatch")
class Employeefullupdate(View):
    def put(self,request,i):
        data=json.load(request.body)

        print(data)
        try:
            e=Employee.objects.get(id=id)

            e.empid=data["empid"]
            e.name=data['name']
            e.age=data['age']
            e.place=data['place']
            e.gender=data['gender']
            e.joining_date=data['joining_date']
            e.salary=data['salary']
            e.designation=data['designation']

            e.save()
            return JsonResponse({"Message":"Updated Successfully"})
        except:
            return JsonResponse({"Message":"No employee Data"})
        

@method_decorator(csrf_exempt,name="dispatch")
class EmployeeDelete(View):
    def delete(self,request,i):
        e=Employee.objects.get(id=i)
        e.delete()
        return JsonResponse({"Message":"Deleted Successfully"})


