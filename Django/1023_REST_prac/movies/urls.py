from django.urls import path
from . import views

app_name='movies'
urlpatterns = [
    path('actor_list/', views.actor_list,),
    path('actor_list/<int:pk>/', views.actor_detail,),
    path('movie_list/', views.movie_list,),
    path('movie_list/<int:pk>/', views.movie_detail,),
    path('review_list/', views.review_list,),
    path('review_list/<int:pk>/', views.review_detail,),
    path('create_review/<int:movie_pk>/', views.create_review,),

]
