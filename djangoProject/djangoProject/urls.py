"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from lab3_web import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.fourth, name='1stpage'),
    path('flowermarket/', views.fourth, name='flowermarket'),
    path('flowers/', views.fifth, name='flowers'),
    path('contactus/', views.sixth, name='contactus'),
    # path('login/', views.seven, name='login'),
    path('payment/', views.eight, name='payment'),
    path('registr/', views.nine, name='registr'),
    path('cart/', views.ten, name='cart'),
    path('', include("django.contrib.auth.urls")),
    path('create_articles', views.create_prod, name='create_articles'),
    path('<int:pk>', views.ArticlesDetailed.as_view(), name='detail_art'),
    path('<int:pk>/update', views.ArticlesUpdate.as_view(), name='update_art'),
    path('<int:pk>/delete', views.ProductsDelete.as_view(), name='del_art'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)