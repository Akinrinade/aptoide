# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.conf.urls import url
from .views import myview


urlpatterns = [

url(
        r'^my-form/$', myview, name='my-form',
    ),
]