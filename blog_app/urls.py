from django.urls import path, re_path
from . import views

app_name = 'blog_app'

urlpatterns = [
    path('', views.PostListView.as_view(),name='post_list'),
    path('about',views.AboutView.as_view(),name='about'),
    re_path(r'^(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='blog_detail'),
]
