"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include, re_path
from myapp.views import *

urlpatterns = [
    #path('hello/',say_hello), # hello/* to match any string
    re_path('hello/(\w+)',say_hello),
    re_path('datetime/(\w+)', current_datetime), #\w+ means only word character
    re_path('offset/(\d+)',hours_ahead),
    path('readhtml/',current_datehtml),
    path('form/',create_form),
    path('admin/', admin.site.urls),
    path('search/',search),
    path('modelform/',register),
    path('getcolor/',getcolor),
    path('setcolor/',set_color),
    path('showcolor/',show_color),
    path('login/',login),
    path('loginuser/',login_user),
    path('logincookie/',login_set_cookie),
    path('showuser/',show_user),
    path('logout/',logout_user),
    path('searchuser/',search_user),
    path('searchcookie/',search_cookie),
    path('savehtml/',savehtml),
    path('upload/',uploadfile)

]
