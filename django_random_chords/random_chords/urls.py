from django.urls import path
from ranchords import views

urlpatterns = [
    path('', views.home, name='home'),
    path('funky_website/', views.funk),
]
