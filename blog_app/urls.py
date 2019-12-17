from django.urls import path, re_path
from . import views

app_name = 'blog_app'

urlpatterns = [
    re_path(r'^(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='blog_detail'),
]
