from django.contrib import admin
from django.urls import include, path

from task_manager import views

urlpatterns = [
    path('', views.BaseView.as_view(), name='base'),
    path('index/', views.get_index, name='index'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),

    path('labels/', include('task_manager.labels.urls')),
    path('tasks/', include('task_manager.tasks.urls')),
    path('users/', include('task_manager.users.urls')),
    path('statuses/', include('task_manager.statuses.urls')),

    path('admin/', admin.site.urls),
]
