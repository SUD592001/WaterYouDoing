from django.urls import path
from evaluator import views

urlpatterns = [
    path('new/', views.evaluate, name='evaluate')
]
