from django.shortcuts import render

def home(request):
    return render(request, "core/inicio.html")

def about(request):
    return render(request, "core/about.html")