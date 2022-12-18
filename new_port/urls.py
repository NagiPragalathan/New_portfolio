"""new_port URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from base import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('home',views.home),
    path('about',views.about),
    path('blog',views.blog),
    path('edit',views.edit),
    path('resume',views.resumes),


    path('del_skill',views.del_skill),
    path('save_skill',views.save_skill),
    path('save_project',views.save_project),
    path('delete_prj',views.delete_prj),
    path('save_atchviements',views.save_atchviements),
    path('del_atc',views.delete_atc),
    path('save_certificate',views.save_certificate),
    path('del_cer',views.delete_cer),
    path('save_hack',views.save_hackthons),
    path('del_hack',views.delete_hackthons),
    path('save_res',views.add_resume),
    path('del_res',views.delete_res),
    path('save_role',views.save_roles),
    path('delete_role',views.delete_role),


]

