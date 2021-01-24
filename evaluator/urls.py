from django.urls import path
from evaluator import views

urlpatterns = [
    path('new/', views.evaluate, name='evaluate'),
    path('main.js', views.evaluate_js),
    path('result/', views.result, name='result')
]
