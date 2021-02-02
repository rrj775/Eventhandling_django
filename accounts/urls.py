from django.urls import path
from . import views




urlpatterns = [
    path('', views.home),
    path('products/', views.products),
    path('customer/', views.customer),
    path('about/', views.about),
    path('update/', views.update),    
]
