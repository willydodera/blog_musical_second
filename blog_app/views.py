from django.shortcuts import render, HttpResponse, redirect
from .models import Post
from .forms import *
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
def post_list(request, page_id):
    posts = Post.objects.all()
    p = Paginator(posts, 4)
    page = p.page(page_id)
    post_list = page.object_list
    previous_page = None
    one_page_less = None
    actual_page = page_id
    next_page = 2
    one_more_page = next_page + 1
    num_pages = p.num_pages
    if actual_page >= 2:
        if page.has_next():
            next_page = page.next_page_number()
            one_more_page = next_page + 1
        if page.has_previous():
            previous_page = page.previous_page_number()
            one_page_less = previous_page - 1
    context = {"posts":post_list, "next":next_page, "previous":previous_page, "actual":actual_page, "num_pages":num_pages, "one_more":one_more_page, "one_less":one_page_less}
    return render(request, "blog_app/pages.html", context)


def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('pages', page_id=1)
        else:
            return HttpResponse("Formulario invalido")
    else:
        form = PostForm()
        return render(request, "blog_app/create_post.html", {"form":form})


def user_posts(request, page_id):
    user = request.user
    posts = Post.objects.filter(author=user)
    p = Paginator(posts, 4)
    page = p.page(page_id)
    post_list = page.object_list
    previous_page = None
    one_page_less = None
    actual_page = page_id
    next_page = 2
    one_more_page = next_page + 1
    num_pages = p.num_pages
    if actual_page >= 2:
        if page.has_next():
            next_page = page.next_page_number()
            one_more_page = next_page + 1
        if page.has_previous():
            previous_page = page.previous_page_number()
            one_page_less = previous_page - 1
    context = {"posts":post_list, "next":next_page, "previous":previous_page, "actual":actual_page, "num_pages":num_pages, "one_more":one_more_page, "one_less":one_page_less}
    return render(request, "blog_app/user_posts.html", context)


def delete_post(request, post_id):
    post = Post.objects.filter(id=post_id)
    if post:
        post.delete()
        messages.success(request, 'Post eliminado correctamente')
        return redirect('user_posts', page_id=1)
    else:
        return HttpResponse("No hay ningun post")


def read_more(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'blog_app/post.html', {"post":post})
    