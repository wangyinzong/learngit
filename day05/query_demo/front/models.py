from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=30)
    pages = models.IntegerField()
    price = models.FloatField()
    rating = models.FloatField()

    class Meta:
        db_table = 'book'
        ordering =[]
class Category(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        db_table = 'category'

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey("Category",on_delete=models.CASCADE,related_query_name="articles")
    creat_time = models.FloatField()
    class Meta:
        db_table= 'article'