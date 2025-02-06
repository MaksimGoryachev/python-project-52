from django.urls import path

from task_manager.users import views

urlpatterns = [
    path('', views.index),
    path('create/', views.UserCreateView.as_view(), name='user_create'),
]
