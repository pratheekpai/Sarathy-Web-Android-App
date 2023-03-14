"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from first_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'index', views.index, name="index"),
    path('admin/', admin.site.urls),
    url(r'login_who', views.login_who, name="login_who"),
    url(r'whosignup', views.whosignup, name="whosignup"),
    url(r'truck_driver_login', views.truck_driver_login, name="truck_driver_login"),
    url(r'seller_login', views.seller_login, name="seller_login"),
    url(r'truck_driver_details', views.truck_driver_details, name="truck_driver_details"),
    url(r'seller_detail', views.seller_details, name="seller_details"),
    url(r'username_pass_seller', views.username_pass_seller, name="username_pass_seller"),
    url(r'username_pass_truckdriver', views.username_pass_truckdriver, name="username_pass_truckdriver"),    
    url(r'truck_details', views.truck_details, name="truck_details"),
    url(r'next', views.next, name="next"),
    url(r'next1', views.next1, name="next1"),
    url(r'signup', views.signup, name="signup"),
    url(r'job_seller', views.job_seller, name="job_seller"),
    url(r'about', views.about, name="about"),
]
