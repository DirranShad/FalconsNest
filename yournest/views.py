from django.shortcuts import render

def index(request):
    return render(request, "yournest/yournest.html")

def loginpage(request):
    return render(request, "yournest/yournest.html")
