# -*- coding: utf-8 -*-
#
# Copyright © 2016 rmad17 <souravbasu17@gmail.com>
#
# Distributed under terms of the MIT license.

"""life URL Configuration

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

from rest_framework.authtoken import views as drf_views

from .views import home, goal_list, goal_detail, register, create_goal

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^register/$', register, name='register'),
    url(r'^login/$', drf_views.obtain_auth_token, name='login'),
    url(r'^(?P<username>[^/]+)/goal/add/$', create_goal, name='create_goal'),
    url(r'^(?P<username>[^/]+)/goals/$', goal_list, name='goals'),
    url(r'^(?P<username>[^/]+)/goal/(?P<uuid>[^/]+)/$', goal_detail,
        name='goal'),
]
