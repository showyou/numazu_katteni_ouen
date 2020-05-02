from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('articles/', views.ArticleListView.as_view(), name='article_list'),
    path('article/<int:pk>/', views.ArticleView.as_view(), name='article'),
    path('shop/<int:pk>/', views.ShopView.as_view(), name='shop'),
]
