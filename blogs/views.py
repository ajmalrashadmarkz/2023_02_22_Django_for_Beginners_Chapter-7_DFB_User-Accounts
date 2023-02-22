from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy
# Create your views here.

def test(request):
    return HttpResponse("<h1> Test </h1> ")

class BlogListView(ListView):
    model = Post

class BlogDetailView(DetailView):
    model = Post

class BlogCreateView(CreateView):
    model = Post
    template_name = "blogs/post_create.html"
    fields = ["title", "author","body"]

class BlogUpdateView(UpdateView):
    model = Post
    template_name = "blogs/post_update.html"
    fields = ["title", "body"]

class  BlogDeleteView(DeleteView):
    model = Post
    template_name = "blogs/post_delete.html"
    success_url = reverse_lazy("post_list")
