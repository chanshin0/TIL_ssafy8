from django.shortcuts import render, redirect
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from .forms import MemoForm
from .models import Memo
# Create your views here.

@require_safe
def index(request):
    memos = Memo.objects.all()
    context = {
        'memos':memos,
    }
    return render(request, 'memos/index.html', context)

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':    # 제출
        form = MemoForm(request.POST)
        if form.is_valid():
            memo = form.save()
            return redirect('memos:detail', memo.pk)
    else:                           # 생성페이지 이동
        form = MemoForm()
    context = {
        'form':form,
    }
    return render(request, 'memos/create.html', context)

@require_safe
def detail(request, pk):
    memo = Memo.objects.get(pk=pk)
    context = {
        'memo':memo,
    }
    return render(request, 'memos/detail.html', context)

@require_http_methods(['GET', 'POST'])
def update(request, pk):
    memo = Memo.objects.get(pk=pk)
    if request.method == 'POST':    # 제출
        form = MemoForm(request.POST, instance=memo)
        if form.is_valid():
            form.save()
            return redirect('memos:detail', memo.pk)
    else:                           # 수정페이지 이동
        form = MemoForm(instance=memo)
    context = {
        'form':form,
        'memo':memo,
    }
    return render(request, 'memos/update.html', context)

@require_POST
def delete(request, pk):
    memo = Memo.objects.get(pk=pk)
    memo.delete()
    return redirect('memos:index')