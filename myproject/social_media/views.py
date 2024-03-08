from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile, Post, Comment, Follow




# Create your views here.
def index(request):
    context = Post.objects.all()
    return render(request, 'index.html', {'data': context})





if __name__=="__main__":
    debug=True