from django.shortcuts import render
from django.views.generic import ListView
from . import models

# Create your views here.
class IndexListView(ListView):
    template_name = 'index.html'
    model = models.Post
    context_object_name = 'posts'
