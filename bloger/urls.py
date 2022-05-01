from django.urls import path

from . import views



urlpatterns = [
    path('', views.home_page, name='home'),
    # path('about.html', views.about, name='about'),
    # path('contact.html', views.contact, name='contact'),
    path('products.html', views.products, name='products'),
    path('products.html/<str:product_category>', views.productsWithCategory, name='products'),
    path('single-product.html/<int:product_id>', views.single_product, name='single-product'),
]

