from .models import Article
from django.shortcuts import render, redirect
from .forms import ArticleForm
from django.views.decorators.http import require_http_methods, require_POST, require_safe # get방식만 받는걸 의미, ~_get보다 이걸 권장
from django.contrib.auth.decorators import login_required

# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

@login_required # 주소창에 직접 입력해서 들어오는거 막을 수 있음
@require_http_methods(['GET', 'POST'])
def create(request):
    # 5. create로 요청을 보냄(POST) => 사용자가 데이터를 입력하고, 저장해달라고 요청(잘못된...)
    # 10. create로 요청을 보냄(POST) => 사용자가 데이터를 입력하고, 저장해달라고 요청(올바른...)
    if request.method == 'POST':    # <-- '제출' 버튼을 클릭했을 때
    # 6. ArticleForm을 인스턴스화(빈종이 + 사용자가 입력한 정보)
    # 11. ArticleForm을 인스턴스화(빈종이 + 사용자가 입력한 정보)
        form = ArticleForm(request.POST)
    # 7. 데이터가 유효한지 검증(검증 실패!)
    # 12. 데이터가 유효한지 검증(검증 성공!)
        if form.is_valid():
            # 13. 데이터를 저장
            form.save()
            # 14. 원하는 경로로 redirect 한다.
            return redirect('articles:index')
  
        

    else:   # method가 POST가 아닐 때(GET일 때) <-- 'new' 버튼을 클릭했을 때, 페이지 이동은 기본적으로 GET방식.
    # 1. 사용자가 create 경로롤 요청을 보냄(GET) => 빈종이 달라!! 요청
    # 2. ArticleForm으로 빈종이 만든다.
        form = ArticleForm()
    # 3. 사용자에게 빈종이를 보내주기 위해서 context 담기
    # 8. 유효한 데이터만 들어있는 종이를 다시 돌려주기 위해 context에 담기
    context = {
        'form':form,
    }
    # 4. 사용자에게 넘겨줌
    # 9. 사용자에게 올바른 데이터만 있는 종이를 다시 넘겨준다. 다시 위로
    return render(request, 'articles/create.html', context)

@require_safe
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=pk)
        article.delete()
        return redirect('articles:index')

@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        form = ArticleForm(data=request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)

    else:   # GET요청일 때 -> 페이지 이동 -> edit버튼 눌렀을 떄
        form = ArticleForm(instance=article)
    context = {
        'form':form,
        'article':article,
    }
    return render(request, 'articles/update.html', context)


# create에 주소쳐서 들어가는걸 막으면 주소가 이렇게 뜨는데
# http://127.0.0.1:8000/accounts/login/?next=/articles/create/
# next는 로그인 하고나서 다음에 이동할 url을 지정해 놓은 것