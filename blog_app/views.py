from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from . import models

# Create your views here.
class IndexListView(ListView):
    template_name = 'index.html'
    model = models.Post
    context_object_name = 'posts'

class PostDetailView(DetailView):
    context_object_name = 'post_detail'
    model = models.Post
    # Need to change the template_name because of change in settings.py file
    template_name = 'blog_app/post_detail.html'

class PostCreateView(CreateView):
    fields = ('author', 'title', 'text')
    model = models.Post

