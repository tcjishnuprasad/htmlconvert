from django.shortcuts import render
from .models import Post
from .forms import PostForm

# Create your views here.

def basic(request):
    form=PostForm()
    return render(request,"convert/home.html",{"form":form})