from django.shortcuts import render

# Create your views here.
foods = ["피자","치킨","국밥","초밥", "민초흑당로제마라탕"]
drinks = ["cider","coke","miranda","fanta", "eye of finetree"]
menu = foods + drinks

def food(request):
    context = {
        'foods':foods,
    }
    return render(request, 'menus/food.html', context)

def receipt(request):
    order = request.GET.get('order')
    context = {
        'order':order,
        'menu':menu,
    }
    return render(request, 'menus/receipt.html', context)

def drink(request):
    context = {
        'drinks':drinks,
    }
    return render(request, 'menus/drink.html', context)