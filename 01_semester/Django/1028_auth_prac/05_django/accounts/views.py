from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm, CustomUserChangeForm

def login(request):
    # 2. POST요청일 때, 어쎈티케이션폼에 사용자 정보를 담은 뒤
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        # 2-1. 유효성 검사
        if form.is_valid():
            # 2-2 유효성 검사를 통과했다면, login함수를 통해 인증된 유저객체를 반환한다.
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
    # 1. get요청일 때 로그인폼을 보여줌(빈 종이)
        form = AuthenticationForm()
    context= {
        'form':form,
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect("articles:index")

# create (user를)
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # 여기에 넣어주면 된다.
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/signup.html', context)

def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('articles:index')

def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
        return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)  
        # 얘는 빈종이아니고 채워줘야함. instance 인자 사용
    context = {
        'form':form,
    }
    return render(request, 'accounts/update.html', context)
