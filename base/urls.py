from django.urls import path
from . import views
# import all functions using the views

urlpatterns = [
    path('', views.home)
]