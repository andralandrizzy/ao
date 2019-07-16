from django.urls import path
from . import views

# Create your views here.

urlpatterns = [
    path('blog/<int:blog_id>', views.blog_detail, name='blog'),
    path('search', views.search, name='search'),
]
