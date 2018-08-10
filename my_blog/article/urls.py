from django.contrib import admin
from django.urls import path, include
from .import views

app_name='article'
urlpatterns = [
 	path('', views.index, name='index'),
    path('list', views.list, name='list'),
    path('<int:id>/', views.detail, name='detail'),
   
  
   # path('', views.test, name='test'),
]
