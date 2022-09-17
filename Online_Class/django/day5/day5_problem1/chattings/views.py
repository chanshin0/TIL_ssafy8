from django.shortcuts import render, redirect
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from .models import Chat
from .forms import ChatForm

# Create your views here.

def index(request):
    chat = Chat.objects.all()
    context = {
        'chat':chat,
    }
    return render(request, 'chattings/index.html', context)

def create(request):
    form = ChatForm()
    context = {
        'form':form,
    }
    return render(request, 'chattings/create.html', context)

def new(request):
    user = request.POST.get('user')
    content = request.POST.get('content')
    chat = Chat(user=user, content=content)
    chat.save()
    
    return redirect('chattings:detail', chat.pk)

@require_safe
def detail(request, pk):
    chat = Chat.objects.get(pk=pk)
    context = {
        'chat':chat,
    }
    return render(request, 'chattings/detail.html', context)

def delete(request, pk):
    chat = Chat.objects.get(pk=pk)
    chat.delete()
    return redirect('chattings:index')