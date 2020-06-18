from django.urls import path
from ranchords import views

urlpatterns = [
    path('', views.home),
    path('what_the_funk/', views.funk),
]
