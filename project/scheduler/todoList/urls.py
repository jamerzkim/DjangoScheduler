from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('check/', views.check),
    path('check/details/', views.details),
    path('template/', views.template),
]