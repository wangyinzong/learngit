from django.db import models
from datetime import datetime
# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,null=False)
    author = models.CharField(max_length=100,null=False)
    price = models.FloatField(default=0)
    # pub_time = models.DateTimeField(auto_now_add=True)
    pub_time = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return "<Book ({name},{author},{price})>".format(name=self.name,author=self.author,price=self.price)
class Publisher(models.Model):
    name = models.CharField(max_length=100,null=False)
    address = models.CharField(max_length=100,null=False)