from django.urls import path
from leaderboard import views

urlpatterns = [
    path('', views.test)
]
