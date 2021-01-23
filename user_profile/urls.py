from django.urls import path
from user_profile import views

urlpatterns = [
    path('<str:username>/', views.view_profile, name='view_profile')
]