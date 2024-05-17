from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
# Create your views here.

def home(request):
    peoples=[
        {'name':'Ayush Shrestha','age':23},
        {'name':'Supriya Shrestha','age':21},
        {'name':'Abhi lama','age':12},
        {'name':'Sravan Ghimirey','age':63},
        {'name':'Sushila suppa','age':34},
        {'name':'Suman Shrestha','age':13},
    ]

    vegetables={'pumpkin','ladyfinger','brinjal','carrots'}
    return render(request,"index.html",context={'peoples':peoples,'vegetables':vegetables})

def contacts(request):
    return render(request,"contacts.html")

def about(request):
    return render(request,'aboutus.html')

def studentList(request):
    students=Student.objects.all().order_by('-date')
    return render(request,'studentlist.html',{'students':students})
def student_page(request,slug):
    student=Student.objects.get(slug=slug)
    return render(request,'student_page.html',{'student':student})

