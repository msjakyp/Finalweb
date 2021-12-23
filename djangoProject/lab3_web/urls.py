from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='4thpage'),
    path('flowermarket/', views.fourth, name='flowermarket'),
    path('flowers/', views.fifth, name='flowers'),
    path('contactus/', views.sixth, name='contactus'),
    path('login/', views.seven, name='login'),
    path('payment/', views.eight, name='payment'),
    path('registr/', views.nine, name='registr'),
    path('cart/', views.ten, name='cart'),
    path('', include("django.contrib.auth.urls")),
    path('create_articles', views.create_prod, name='create_articles'),
    path('<int:pk>', views.ArticlesDetailed.as_view(), name='detail_art'),
    path('<int:pk>/update', views.ArticlesUpdate.as_view(), name='update_art'),
    path('<int:pk>/delete', views.ProductsDelete.as_view(), name='del_art'),
]