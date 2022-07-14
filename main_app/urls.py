from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    
    
    
    
    path('resources/', views.resourceIndex, name='resource_list'),
    
    path('resources/<int:resource_id>/', views.resourceDetail, name='resource_detail'),
    
    path('resources/create/', views.ResourceCreate.as_view(), name='resources_create'),
    
    path('resources/<int:pk>/update/', views.ResourceUpdate.as_view(), name='resources_update'),
    
    path('resources/<int:pk>/delete/', views.ResourceDelete.as_view(), name='resources_delete'),
    
    
    path('accounts/', include('django.contrib.auth.urls')),
    
    path('accounts/signup/', views.signup, name='signup'),


    # path('course-details/', views.course_details, name='course-details'),
    
    # path('class-material/', views.class_material, name='class-material'),


]