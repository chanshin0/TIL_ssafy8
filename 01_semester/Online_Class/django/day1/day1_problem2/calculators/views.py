from django.shortcuts import render

# Create your views here.

def calculation(request):
    return render(request, 'calculation.html')

def result(request):
    num1 = int(request.GET.get('num1'))
    num2 = int(request.GET.get('num2'))
    plus = num1 + num2
    minus = num1 - num2
    times = num1 * num2
    if num2 == 0:
        divide = '계산할 수 없습니다.'
    else:
        divide = num1 / num2
    context = {
        'num1':num1,
        'num2':num2,
        'plus':plus,
        'minus':minus,
        'times':times,
        'divide':divide,
    }
    return render(request, 'result.html', context)
