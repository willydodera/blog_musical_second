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
            return redirect('pages')
        else:
            return HttpResponse("Formulario invalido")
    else:
        form = PostForm()
        return render(request, "blog_app/create_post.html", {"form":form})


def user_posts(request):
    user = request.user
    posts = Post.objects.filter(author=user)
    return render(request, "blog_app/user_posts.html", {"posts":posts, "user":user})


def delete_post(request, post_id):
    post = Post.objects.filter(id=post_id)
    if post:
        post.delete()
        messages.success(request, 'Post eliminado correctamente')
        return redirect('user_posts')
    else:
        return HttpResponse("No hay ningun post")


def read_more(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'blog_app/post.html', {"post":post})
    

