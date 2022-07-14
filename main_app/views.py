from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Resources

def home(request):
    return render(request, 'home.html')

@login_required
def resourceIndex(request):
    resources = Resources.objects.filter(user=request.user)
    return render(request, 'main_app/resources.html', {'resources': resources} )

def resourceDetail(request, resource_id):
    resources = Resources.objects.get(id=resource_id)
    return render(request, 'main_app/resources_detail.html', {'resources':resources})

class ResourceCreate(LoginRequiredMixin, CreateView):
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

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

def course_details(request):
    return render(request, 'course-details.html')

def class_material(request):
    return render(request, 'class-material.html')