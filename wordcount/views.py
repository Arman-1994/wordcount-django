from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    params = {"name":"Arman"}
    return render(request,"home.html",params)

def eggs(request):
    return HttpResponse("Thanks for the Eggs")

def count(request):
    text = request.GET["fulltext"]
    splited = text.split()
    length = len(splited)
    print(length)
    return render(request,"count.html",{"word_count":length,"og_text":text})