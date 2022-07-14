from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Resources

def home(request):
    return render(request, 'home.html')

def resourceIndex(request):
    resources = Resources.objects.all()
    return render(request, 'main_app/resources.html', {'resources': resources} )

def resourceDetail(request, resource_id):
    resources = Resources.objects.get(id=resource_id)
    return render(request, 'main_app/resources_detail.html', {'resources':resources})

class ResourceCreate(CreateView):
    model = Resources
    fields = '__all__'
    success_url = '/resources/'
    
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ResourceUpdate(UpdateView):
    model = Resources
    fields = ['resource_title','resource_link','resource_description']
    success_url = '/resources/'

class ResourceDelete(DeleteView):
    model = Resources
    success_url = '/resources/'


def course_details(request):
    return render(request, 'course-details.html')

def class_material(request):
    return render(request, 'class-material.html')

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')
