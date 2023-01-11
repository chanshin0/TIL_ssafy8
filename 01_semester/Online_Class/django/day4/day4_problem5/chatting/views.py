from django.shortcuts import render, redirect
from .models import Chat

# Create your views here.

def index(request):
    chattings = Chat.objects.all()
    context = {
        'chattings':chattings,
    }

    return render(request, 'chatting/index.html', context)

def new(request):
    return render(request, 'chatting/new.html', )

def create(request):
    user = request.POST.get('user')
    content = request.POST.get('content')
    chatting = Chat(user=user, content=content)
    chatting.save()
    return redirect('chatting:index',)

def detail(request, pk):
    chatting = Chat.objects.get(pk=pk)
    context = {
        'chatting':chatting,
    }

    return render(request, 'chatting/detail.html', context)

def edit(request, pk):
    chatting = Chat.objects.get(pk=pk)
    context = {
        'chatting':chatting,
    }

    return render(request, 'chatting/edit.html', context)

def update(request, pk):
    chatting = Chat.objects.get(pk=pk)
    chatting.user = request.POST.get('user')
    chatting.content = request.POST.get('content')
    chatting.save()
    return redirect('chatting:detail', pk)

def delete(request, pk):
    chatting = Chat.objects.get(pk=pk)
    chatting.delete()
    return redirect('chatting:index',)