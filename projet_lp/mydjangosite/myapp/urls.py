"""
URL configuration for mydjangosite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from myapp import views 

urlpatterns = [
    path("", views.index, name='index'),
     path("signup/", views.signaction, name='signup'),
     path('login/', views.login, name='login'),  
    path("welcome/", views.welcome, name='welcome'),
    path("welcome_admin/", views.welcome_admin, name='welcome_admin'),
    
    path('', views.static, name='static'),
    path('signout/', views.signout, name='signout'),
    path('tab_users/', views.tab_users, name='tab_users'),
     
    path('add-user/', views.add_user, name='add_user'),
    path('user_del/', views.user_del, name='user_del'),
    path('user_update/', views.user_update, name='user_update'),
    
]
# serve static files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

