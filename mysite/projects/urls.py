from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.ProjectListView.as_view(), name="projects"),
    path('user_projects', views.UserProjectListView.as_view(), name="user_projects"),
]
