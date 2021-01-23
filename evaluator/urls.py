from django.urls import path
from evaluator import views

urlpatterns = [
    path('new/', views.evaluate),
    path('main.js', views.evaluate_js),
]
