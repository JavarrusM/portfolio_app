from django.urls import path
from . import views

app_name = "analysis"

urlpatterns = [
    path('', views.all_analyses, name="all_analyses"),
    path('<int:analysis_id>/', views.detail, name='detail'),
]
