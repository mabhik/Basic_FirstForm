from django.shortcuts import render

# Create your views here.

def firstform(request):
    return render(request,'firstform.html')