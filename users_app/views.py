from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from blog_app.models import Post
from .forms import UserRegisterForm, UserEditForm
from .models import Avatar


# Create your views here.
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contraseña)
            if user is not None:
                login(request, user)
                posts = Post.objects.all()
                return render(request, "blog_app/pages.html", {"form":form, "mensaje":f"Bienvenido {usuario}", "posts":posts})
            else:
                return render(request, "users_app/login.html", {"form":form, "mensaje":"Usuario o contraseña incorrectos"})
        else:
            return render(request, "users_app/login.html", {"form":form, "mensaje":"Formulario invalido"})
    form = AuthenticationForm()
    return render(request, "users_app/login.html", {"form":form})


def logout(request):
    logout(request)


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            user = User.objects.get(username=username)
            avatar = Avatar(user=user)
            avatar.save()
            form = AuthenticationForm()
            msj = f"Usuario {username} creado con éxito"
            context = {"form": form, "msj":msj}
            return render(request, "main_app/home.html", context)
        else:
            return HttpResponse("Formulario invalido")
    else:
        form = UserRegisterForm()
        context = {"form": form}
        return render(request, "users_app/register.html", context)


def delete_user(request):
    user = request.user
    user.delete()
    return redirect('logout')


def profile(request):
    user = User.objects.get(username=request.user)
    img = Avatar.objects.filter(user=user)
    if img:
        img = (Avatar.objects.filter(user=user))[0].img.url
    context = {"user":user, "img":img}
    return render(request, "users_app/profile.html", context)


def edit_profile(request):
    user = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            info = form.cleaned_data
            user.username = info["username"]
            user.email = info["email"]
            user.first_name = info["first_name"]
            user.last_name = info["last_name"]
            user.password1 = info["password1"]
            user.password2 = info["password2"]
            user.save()
            old_avatar = Avatar.objects.get(user=user)
            if old_avatar.img:
                old_avatar.delete()
            avatar = Avatar(user=user, img=info["avatar"])
            avatar.save()
            img = avatar.img.url
            msj = f"Usuario {user.username} editado con éxito"
            context = {"msj":msj, "user":user, "img":img}
            return render(request, "users_app/profile.html", context)
    else:
        form = UserEditForm(instance=user)
        context = {"form": form}
        return render(request, "users_app/edit_profile.html", context)


