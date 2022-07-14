from django.db import models
from django.contrib import admin
from django.urls import reverse

class Resources(models.Model):
    resource_title = models.CharField(max_length=100)
    resource_link = models.CharField(max_length=500)
    resource_description = models.TextField(max_length=500)
    
    def __str__(self):
        return f'{self.resource_title} {self.resource_link} {self.resource_description}'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'resource_id': self.id})