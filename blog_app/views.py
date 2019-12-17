from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . import models

# Create your views here.
class IndexListView(ListView):
    template_name = 'index.html'
    model = models.Post
    context_object_name = 'posts'

class PostDetailView(DetailView):
    context_object_name = 'post_detail'
    model = models.Post
    template_name = 'blog_app/post_detail.html'
