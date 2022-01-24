from audioop import reverse
from dataclasses import field
from statistics import mode
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

from blogapp.models import Category, Post
from .forms import PostForm,EditForm





class HomeView(ListView):
    model = Post
    template_name = "home.html"
    ordering = ['date_added']

class ArticleDetailView(DetailView):
    model = Post
    template_name = "article_details.html"

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"
 

class UpdatePostView(UpdateView):
    model = Post
    template_name = "update_post.html"
    form_class = EditForm
   

class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy('home')
  
def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats)
    return render(request, 'categories.html',{'category_posts':category_posts})

