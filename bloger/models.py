from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50,primary_key=True)
    
    def __str__(self):
         return self.name

class Product(models.Model):
    name = models.CharField(max_length=50,unique=True)
    desc = models.TextField(max_length=5000)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)
    cat = models.ForeignKey(Category,related_name='product_category',on_delete=models.CASCADE)
    product_thumnail = models.ImageField(upload_to='uploads/')
    product_cover_image = models.ImageField(upload_to='uploads/')

# class Review(models.Model):
#     message = models.TextField(max_length=500)
#     create_at = models.DateTimeField(auto_now_add=True)
#     product = models.ForeignKey(Product,related_name='review',on_delete=models.CASCADE)
#     user = models.ForeignKey(User,related_name='review',on_delete=models.CASCADE)

    



# class Category(models.Model):
#     category = models.CharField(
#         max_length=400, verbose_name='النوع', primary_key=True)

#     def __str__(self):
#         return self.category

# class Product(models.Model):
#     product_name = models.CharField(max_length=500)
#     article_caption = models.TextField(max_length=10000)
#     article_category = models.ForeignKey(
#         Category, on_delete=models.CASCADE, default=None)
#     
#     aritcle_thumbnail = models.ImageField(upload_to='uploads/')
#     pub_date = models.DateTimeField()

#     def __str__(self):
#         return self.article_title

