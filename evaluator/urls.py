from django.urls import path
from evaluator import views

urlpatterns = [
    path('new/', views.evaluate, name='evaluate'),
    path('detail/<str:username>/', views.detail, name='detail'),
    path('result/', views.result, name='result'),
    path('result/<str:username>/', views.result, name='result'),
    path('result/learn-more/', views.learn_more, name='learn_more'),
]
