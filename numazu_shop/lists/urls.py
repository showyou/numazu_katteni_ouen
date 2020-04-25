from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('article/<int:article_id>/', views.article, name='article'),
    path('shop/<int:shop_id>/', views.shop, name='shop'),
]
