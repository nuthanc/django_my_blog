from django.shortcuts import render
from django.views.generic import (
    ListView, DetailView, CreateView, TemplateView)
from blog_app.models import Post, Comment

# Create your views here.
class AboutView(TemplateView):
    template_name = 'about.html'
class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now().order_by('-published_date'))
class PostDetailView(DetailView):
    context_object_name = 'post_detail'
    model = models.Post
    # Need to change the template_name because of change in settings.py file
    template_name = 'blog_app/post_detail.html'

class PostCreateView(CreateView):
    fields = ('author', 'title', 'text')
    model = models.Post

