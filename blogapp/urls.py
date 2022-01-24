from django.urls import path
from . views import AddPostView, HomeView,ArticleDetailView,UpdatePostView,DeletePostView
from django import views
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="detail"),
    path('add/', AddPostView.as_view(), name="add_post"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update"),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name="delete"),
]