"""
URL configuration for market_magician project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from predictions import views

from .views import predict_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.index, name='index'),
    path('page_test/', views.page_test, name='page_test'),
    path('add_to_watchlist/', views.add_to_watchlist, name='add_to_watchlist'),
    path('view_watchlist/', views.view_watchlist, name='view_watchlist'),
    path('accounts/', include('django.contrib.auth.urls')),
    """
    ####added this path to comunicate with the function I created we probably need to clean up some of the urls###
    
    path('api/predict/', predict_view, name='predict'),
    """
]
