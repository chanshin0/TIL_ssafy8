from multiprocessing import context
from django.shortcuts import render, redirect

import articles
from .models import Article

# Create your views here.

def index(request):
    # 최신글 순서로 정렬하기
    articles = Article.objects.all()[::-1]
    # articles = Article.objects.order_by('-pk')

    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    article = Article(title=title, content=content)
    article.save()

    # Article.objects.create(title=title, content=content)

    # return render(request, 'articles/create.html')
    # return redirect('articles:index')
    return redirect('articles:detail', article.pk)

def detail(request, pk):
    article = Article.objects.get(pk=pk) # db-인자
    context = {
        'article':article,
    }
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()

    return redirect('articles:index')

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article':article,
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)

    article.title = request.POST.get('title') 
    # 새로 입력한 title을 기존 데이터에 덮어쓰기
    article.content = request.POST.get('content') 
    article.save() # DB에 데이터 저장

    return redirect('articles:detail', article.pk)