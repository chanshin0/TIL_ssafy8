from django.shortcuts import render

# Create your views here.

def dinner(request, menu, members):
    context = {
        'menu':menu,
        'members':members,
    }

    return render(request, 'dinner.html', context)