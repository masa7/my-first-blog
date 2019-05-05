# -*- coding: utf-8 -*-
"""
Created on Fri May  3 20:31:58 2019

@author: MaSa
"""
from django.urls import path
from . import views

urlpatterns = [
        path('', views.post_list, name='post_list'),
        ]
