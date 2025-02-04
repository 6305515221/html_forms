"""
URL configuration for createmodels project.

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
from django.urls import path

from ap1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("insert_topic/",insert_topic,name='insert_topic'),
    path("insert_webpage/",insert_webpage,name='insert_webpage'),
    path("insert_acees/",insert_acees,name='insert_acees'),
    path("display_topic/",display_topic,name='display_topic'),
    path("display_webpage/",display_webpage,name='display_webpage'),
    path("display_acess/",display_acess,name='display_acess'),
    # path("front_topic1/",front_topic1,name="front_topic1"),
    path("front_topic/",front_topic,name="front_topic"),
    path("front_webpage/",front_webpage,name='front_webpage'),
    path("front_acess/",front_acess,name='front_acess'),
    path("select_multiple/",select_multiple,name="select_multiple"),
    path("checkbox_view/",checkbox_view,name='checkbox_view'),
]
