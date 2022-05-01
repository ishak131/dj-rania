import os
from unicodedata import category
# from unicodedata import category
# from urllib import response
from django.conf import settings
from django.shortcuts import render

from bloger.models import Product
# from bloger.models import Article, Category, ImagesManager, Languages

print(settings.BASE_DIR)
def home_page(request):
    return render(request,'index.html')

# def about(request):
#     return render(request,'about.html')

# def contact(request):
#     return render(request,'contact.html')

def products(request):
    allProducts = Product.objects.order_by('-create_at') 
    return render(request,'products.html' ,  {'products': allProducts})

def productsWithCategory(request,product_category):
    allProducts = Product.objects.filter(cat = product_category) 
    print(product_category)
    print(allProducts)
    return render(request,'products.html' ,  {'products': allProducts})

def single_product(request,product_id):
    my_product = Product.objects.get(id=product_id)
    my_products = Product.objects.filter(cat=my_product.cat)
    return render(request,'single-product.html' , {'single_product' :my_product,"similar_products":my_products })

# def home_page_category(request, lang_code,category):
#     latest_Article_list = Article.objects.filter(article_lang=lang_code,article_category=category)
#     categories = Category.objects.all()[:5]
#     languages = Languages.objects.all()
#     return render(request,'index.html',
#     {
#     "articles":latest_Article_list ,
#     "categories":categories,
#     "languages":languages,
#     "request":request,
#     })
# # Create your views here.


# def single_article(request,lang_code, article_link):
#      article = Article.objects.get(article_link=article_link,article_lang=lang_code)
#      languages = Languages.objects.all()
#      categories = Category.objects.all()[:5]
#      return render(request,'single_article.html',
#     {
#     "categories":categories,
#     "article":article,
#     "languages":languages,
#     "request":request,
#     })

# # Create your custom error here.
# def custom_page_not_found_view(request, exception):
#     response = redirect('/EN')
#     return response

# def custom_error_view(request, exception=None):
#     response = redirect('/EN')
#     return response

# def custom_permission_denied_view(request, exception=None):
#     response = redirect('/EN')
#     return response

# def custom_bad_request_view(request, exception=None):
#     response = redirect('/EN')
#     return response