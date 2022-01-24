from random import choice

from django import forms
from .models import Category, Post

choices = Category.objects.all().values_list("name", "name")

choice_list = []
for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ( 'author','title','trailer_link', 'body','header_image')

        widgets= {
          
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Enter Movie Title'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Enter Movie Title'}),
            'trailer_link': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Enter Movie Title'}),
            'body': forms.Textarea(attrs={'class': 'form-control','placeholder' : 'Enter Description'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author','title','trailer_link', 'body')

        widgets= {
            #'author': forms.Select(attrs={'class': 'form-control','placeholder' : 'Enter Author'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Enter Movie Title'}),
            'trailer_link': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Enter Movie Title'}),
            'body': forms.Textarea(attrs={'class': 'form-control','placeholder' : 'Enter Description'}),
        }