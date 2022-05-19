from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.ProjectListView.as_view(), name="projects"),
    path('projects/<int:pk>', views.ProjectDetailView.as_view(), name="project"),
    path('user_projects', views.UserProjectListView.as_view(), name="user_projects"),
    path('projects/<int:pk>/update', views.ProjectUpdateView.as_view(), name="project_update"),
    path('project/<int:pk>/delete', views.ProjectDeleteView.as_view(), name='project_delete'),
    path('new_project/', views.ProjectCreateView.as_view(), name='new_project'),
]
