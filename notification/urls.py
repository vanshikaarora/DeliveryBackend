from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.homePageView, name='home'),
    path(r'insert/', views.fcm_insert, name='insert'),
    path(r'send/', views.send_notifications, name='send'),
    path(r'add_user/',views.add_user,name='add_user'),
    path(r'check/',views.check_credentials,name='check')
]