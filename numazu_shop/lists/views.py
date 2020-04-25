from django.shortcuts import get_object_or_404, render
from django.http import Http404

from .models import Article, Shop

def index(request):
    latest_article_list = Article.objects.order_by('-pub_date')[:5]
    shops = Shop.objects.all()
    return render(request, 'lists/index.html', {'latest_article_list': latest_article_list, 'shops': shops })


def article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'lists/article.html', {'article': article })


def shop(request, shop_id):
    shop = get_object_or_404(Shop, pk=shop_id)
    return render(request, 'lists/shop.html', {'shop': shop })
