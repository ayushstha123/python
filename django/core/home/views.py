from django.shortcuts import render
from django.http import HttpResponse
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
