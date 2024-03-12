from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile, Post, Comment, Follow




# Create your views here.
def index(request):
    context = Post.objects.all()
    return render(request, 'index.html', {'data': context})


def create_user(request):
    if request.method == "POST":
        username = request.POST.get('username')  # Use POST method to retrieve form data
        password = request.POST.get('password')  # Use POST method to retrieve form data
        new_user = User.objects.create_user(username=username, password=password)
        new_user.save()
        return redirect('index')  # Redirect to index page 
    else:
        return render(request, 'create_user.html', {})
 



if __name__=="__main__":
    debug=True