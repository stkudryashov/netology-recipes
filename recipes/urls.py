from django.urls import path
from calculator import views

urlpatterns = [
    path('<str:dish>/', views.recipe)
]
