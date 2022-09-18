from django.shortcuts import render

# Create your views here.

def first(request):
    third = request.GET.get('third')
    context = {
        'third':third
    }
    return render(request, 'first.html', context)

def second(request):
    first = request.GET.get('first')
    context = {
        'first':first
    }
    return render(request, 'second.html', context)

def third(request):
    second = request.GET.get('second')
    second2 = request.GET.get('second2')
    s_list = [second, second2]
    context = {
        's_list':s_list,
    }
    return render(request, 'third.html', context)