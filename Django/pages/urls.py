from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
     # http://127.0.0.1:8000/index/ 이렇게 요청오면 views.index를 실행시켜라
    path('greeting/', views.greeting, name='greeting'),
    path('dinner/', views.dinner, name='dinner'),
    path('image/', views.image, name='image'),
    path('temlplate_language/', views.temlplate_language),
    path('throw/', views.throw, name=''),
    path('catch/', views.catch, name=''),
    path('hello/<str:name>/<int:age>', views.hello, name=''),
    # path('hello/<name>', views.hello), 위와 같은 코드
]
