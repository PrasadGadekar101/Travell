from django.urls import path
from HomePage import views

urlpatterns = [
    path('home', views.homepage)
]