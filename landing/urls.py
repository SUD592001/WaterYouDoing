from django.urls import path
from landing import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('accounts/signup/', views.signup, name='signup')
]
