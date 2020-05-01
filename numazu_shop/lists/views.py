from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.views import generic

from .models import Article, Shop

def index(request):
    latest_article_list = Article.objects.order_by('-pub_date')[:15]
    shops = Shop.objects.all()
    return render(request, 'lists/index.html', {'latest_article_list': latest_article_list, 'shops': shops })


class ArticleView(generic.DetailView):
    model = Article
    template_name = 'lists/article.html'


class ShopView(generic.DetailView):
    model = Shop
    template_name = 'lists/shop.html'


