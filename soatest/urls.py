"""soatest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from yml import views as yml_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^list/$', yml_views.list, name='list'), 
    url(r'^$', yml_views.index),
    url(r'^list/spot/(\d+)/$', yml_views.item, name='item'),
    url(r'^save_profile/', yml_views.save_profile, name='save_profile'),
]
