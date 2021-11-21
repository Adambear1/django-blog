from django.urls import path
from blogging.views import ListView, DetailView

urlpatterns = [
    path('', ListView.as_view(), name="blog_index"),
    path('posts/<int:pk>/', DetailView.as_view(), name="blog_detail"),
]
