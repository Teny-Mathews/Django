from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View

class Goodmorning(View):

    def get(self,request):
        data={'Message':"Good Morning"}
        return JsonResponse(data)

class Helloworld(View):

    def get(self,request):
        data={'Message':"Hello world"}
        return JsonResponse(data)

class Goodevening(View):

    def get(self,request):
        data={'Message':"Good Evening"}
        return JsonResponse(data)

class Userdetails(View):
    
    def get(self,request):
        data=[

            {"name":"John","age":23,"place":"Ekm"},
            {"name":"Arun","age":25,"place":"Ktm"},
            {"name":"Reyan","age":20,"place":"Ekm"}
        ]
        return JsonResponse(data,safe=False)

from myapp.models import Student

class StudentList(View):
    
    def get(self,request):
        s=Student.objects.all().values()
        print(s)
        print(type(s))

        s=Student.objects.all()
        print(s)
        print(type(s))

        data=list(Student.objects.all().values())
        print(data)
        print(type(data))

        return JsonResponse(data,safe=False)


from json import loads
import json

@method_decorator(csrf_exempt,name="dispatch")
class StudentCreate(View):
    def post(self,request):

        data=loads(request.body)

        r=data["rollno"]
        n=data["name"]
        a=data["age"]
        p=data["place"]
        m=data["marks"]

        s=Student.objects.create(rollno=r,name=n,age=a,place=p,marks=m)
        s.save()

        return JsonResponse({"message":"Inserted Data Successfully"})

    
@method_decorator(csrf_exempt,name="dispatch")
class StudentDetail(View):
    
    def get(self,request,i):
        s=list(Student.objects.filter(id=i).values())
        if s:
            return JsonResponse(s,safe=False)
        else: 
            return JsonResponse({"Message":"No Student Data"})


@method_decorator(csrf_exempt,name="dispatch")
class StudentDelete(View):
    def delete(self,request,i):
        s=Student.objects.get(id=i)
        s.delete()
        return JsonResponse({"Message":"Deleted Successfully"})

@method_decorator(csrf_exempt,name="dispatch")
class Studentfullupdate:
    def put(self,request,i):
        data=json.load(request.body)

        print(data)
        try:
            s=Student.objects.get(id=id)

            s.name=data['name']
            s.age=data['age']
            s.place=data['place']
            s.marks=data['marks']
            s.save()
            return JsonResponse({"Message":"Updated Successfully"})
        except:
            return JsonResponse({"Message":"No Student Data"})


@method_decorator(csrf_exempt,name="dispatch")    
class Studentpartialupdate:
    def patch(self,request,i):
        data=json.loads(request.body)
        try:
            s=Student.objects.get(id=id)
            if 'rollno' in data:
                s.rollno=data['rollno']

            if 'name' in data:
                s.name=data['name']

            if 'age' in data:
                s.age=data['age']

            if 'place' in data:
                s.place=data['place']

            if 'marks' in data:
                s.marks=data['marks']

            s.save()

            return JsonResponse({"Message":"Updated Partially"})

        except:
            return JsonResponse({"Message":"No Student Data"})


