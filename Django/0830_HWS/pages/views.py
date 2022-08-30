from django.shortcuts import render

# Create your views here.
def dinner(request):
    return render(request, 'dinner.html')