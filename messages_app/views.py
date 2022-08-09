from django.shortcuts import render, redirect
from .models import Message
from .forms import *
from django.db.models import Q
from django.contrib.auth.models import User

# Create your views here.
def inbox(request):
    messages = Message.objects.filter(Q(sender=request.user) | Q(receiver=request.user))
    added = []
    last_messages = []
    for message in messages:
        if message.sender == request.user and message.receiver not in added:
            added.append(message.receiver)
        elif message.receiver == request.user and message.sender not in added:
            added.append(message.sender)

    for user in added:
        last_chat_message = Message.objects.filter(Q(sender=user) | Q(receiver=user)).last()
        last_messages.append(last_chat_message)
    return render(request, 'messages_app/inbox.html', {"messages":last_messages})


def chat(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            receiver = User.objects.get(id=user_id)
            msg = Message(sender=request.user, receiver=receiver, content=info["content"])
            msg.save()
    
    messages = Message.objects.filter(Q(sender=user, receiver=request.user) | Q(sender=request.user, receiver=user))
    form = MessageForm()
    return render(request, 'messages_app/chat.html', {"messages":messages, "form":form})


def new_message(request):

    if request.method == "POST":
        form = UserSearchForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            username = info["username"]
            searched_user = User.objects.filter(username__contains=username)
            return render(request, 'messages_app/new_message.html', {"form":form, "users":searched_user})

    else:
        form = UserSearchForm()
    return render(request, 'messages_app/new_message.html', {"form":form})
        






"""

(Q(sender=user, receiver=request.user) | Q(sender=request.user, receiver=user))

    for message in messages:
        if message.receiver not in added:
            added.append(message.receiver)

"""