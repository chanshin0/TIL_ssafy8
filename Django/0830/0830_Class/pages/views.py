from calendar import c
from multiprocessing import reduction
from django.shortcuts import render
import random
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'index.html')

def greeting(request):
    foods = ['apple', 'banana', 'coconut']
    info = {
        'name': 'chan'
    }
    context = {
        'foods' : foods,
        'info' : info,
    }
    return render(request, 'greeting.html', context)

def dinner(request):
    menu = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)
    context = {
        'pick' : pick
    }
    return render(request, 'dinner.html', context)

def image(request):
    return render(request, 'image.html')

def temlplate_language(request):
    menu = ['족발', '햄버거', '치킨', '초밥']
    my_sentence = 'Life is short, you need python'
    message = ['apple', 'banana', 'cucmber', 'mango']
    empty_list = []
    detetimenow = datetime.now()
    context = {
        'menus' : menu,
        'my_sentence' : my_sentence,
        'messages' : message,
        'empty_list' : empty_list,
        'datetimenow' : detetimenow
    }

    return render(request, 'temlplate_language.html', context)

def throw(request):
    return render(request, 'throw.html')

def catch(request):
    message = request.GET.get('message')
    context = {
        'message':message,
    }
    return render(request, 'catch.html', context)

def hello(request, name, age):
    context = {
        'name':name,
        'age':age,
    }
    return render(request, 'hello.html', context)
