# Author: Thanh HoangVan 
# Email: thanh.hoangvan051199@gmail.com
# Ha noi University of Science and Technology

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login),
    path('analysis/', views.Analysis),
    path("input/", views.InputData),
    path("home/", views.Databoard),
    path("analysis/result/", views.ResultAnalysis),
]
