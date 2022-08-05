from django.shortcuts import render, HttpResponse, redirect
from .models import Post
from .forms import *
from django.contrib import messages

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, "blog_app/pages.html", {"posts":posts})


def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Post creado!")
            return redirect('pages')
        else:
            return HttpResponse("Formulario invalido")
    else:
        form = PostForm()
        return render(request, "blog_app/create_post.html", {"form":form})

