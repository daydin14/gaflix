from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('resources/', views.resourceIndex, name='resource_list'),
    
    path('resources/<int:resource_id>', views.resourceDetail, name='resource_detail'),
    
    path('course-details/', views.course_details, name='course-details'),
    
    path('class-material/', views.class_material, name='class-material'),

    path('login/', views.login, name='login'),
    
    path('signup/', views.signup, name='signup')
]