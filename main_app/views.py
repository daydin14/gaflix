
from django.shortcuts import render
from .models import Resources

def home(request):
    return render(request, 'home.html')

def resources(request):
    resources = Resources.objects.all()
    return render(request, 'resources.html', {'resources': resources} )

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def course_details(request):
    return render(request, 'course-details.html')

def class_material(request):
    return render(request, 'class-material.html')