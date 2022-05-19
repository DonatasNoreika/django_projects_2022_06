from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProjectListView.as_view(), name="projects"),
    path('register/', views.register, name='register'),
]
