from django.shortcuts import render

# Create your views here.

def calculation(request):
    return render(request, 'calculation.html')

def result(request):
    rst = request.Get.get('')
    context = {
        'result':rst
    }
    return render(request,  'result.html')
