from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('<int:page_id>', views.post_list, name="pages"),
    path('create/', views.create_post, name="create"),
    path('user_posts/<int:page_id>', views.user_posts, name="user_posts"),
    path('delete_post/<int:post_id>', views.delete_post, name="delete_post"),
    path('read_more/<int:post_id>', views.read_more, name="read_more"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)