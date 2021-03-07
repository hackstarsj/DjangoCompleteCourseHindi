"""DjangoHindiTutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from DjangoHindiApp import views
from django.conf.urls.static import static
from DjangoHindiTutorial import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("demoPage",views.demoPage),
    path("demoPage2",views.demoPage2),
    path('',views.loginUser,name="login"),
    path('signup',views.signupUser,name="signup"),
    path('signup_process',views.signup_process,name="signup_process"),
    path('login_proces',views.login_proces,name="login_proces"),
    path('home',views.home,name="home"),
    path('logout',views.logoutUser,name="logout"),
    path('add_tasks',views.add_tasks,name="add_tasks"),
    path('delete/<str:id>',views.delete_task,name="delete_task"),
    path('edit_task/<str:id>',views.edit_task,name="edit_task"),
    path('edit_tasks_save/<str:id>',views.edit_tasks_save,name="edit_tasks_save"),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
