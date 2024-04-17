from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('display_result/', views.display_result, name='display_result'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]