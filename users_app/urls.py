from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', views.login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name='main_app/home.html'), name='logout'),
    path('register/', views.register, name="register"),
    path('delete_user/', views.delete_user, name="delete_user"),
    path('profile/', views.profile, name="profile"),
    path('edit_profile/', views.edit_profile, name="edit_profile"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)