from django.contrib import admin 
from django.urls import path, include
from . import views
  
urlpatterns = [ 
    path('items/', views.MenuItemView.as_view()),
    path('items/<int:pk>', views.SingleMenuItemView.as_view()),
]