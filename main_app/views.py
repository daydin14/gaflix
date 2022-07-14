from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Resources

def home(request):
    return render(request, 'home.html')

def resourceIndex(request):
    resources = Resources.objects.all()
    return render(request, 'resources.html', {'resources': resources} )

def resourceDetail(request, resource_id):
    resources = Resources.objects.get(id=resource_id)
    return render(request, 'resource-details.html', {'resources':resources})



# def addResource(request):
#     return render(request, 'addResource.html')

class ResourceCreate(CreateView):
    model = Resources
    fields = '__all__'
    success_url = '/resources/'




def course_details(request):
    return render(request, 'course-details.html')

def class_material(request):
    return render(request, 'class-material.html')

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')
