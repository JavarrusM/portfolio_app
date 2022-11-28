from django.urls import path
from . import views

app_name = 'generator'

urlpatterns = [
    path('', views.home, name='generator_home'),
    path('about/', views.about, name='generator_about'),
    path('password/', views.password, name='generator_password'),
]