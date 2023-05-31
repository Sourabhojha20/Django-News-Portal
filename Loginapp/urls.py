from django.contrib import admin
from django.urls import path
from Loginapp import views

urlpatterns = [
    path('adminlogin/',views.Userlogin,name='Userlogin'),
    path('logout',views.Logout,name='Logout')
]

