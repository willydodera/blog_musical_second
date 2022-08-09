from django.urls import path
from . import views

urlpatterns = [
    path('', views.inbox, name="inbox"),
    path('chat/<int:user_id>', views.chat, name="chat"),
    path('new_message/', views.new_message, name="new_message"),
]