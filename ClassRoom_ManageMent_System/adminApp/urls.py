from django.urls import path
from . import views
from django.conf.urls import url
urlpatterns =[
    path('',views.index,name="index"),
    url(r'^insert$', views.insert, name='insert'),
    url(r'^insertnotice$', views.insertnotice, name='insertnotice'),
    url(r'^insertfaculty$', views.insertfaculty, name='insertfaculty'),
]