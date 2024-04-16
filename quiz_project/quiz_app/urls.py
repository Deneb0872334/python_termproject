from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('display_result/', views.display_result, name='display_result'),
]