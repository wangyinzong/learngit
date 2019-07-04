from django.db import models

# Create your models here.
class FrontUser(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return "<id:%s,name:(name:%s)>" % (self.id,self.name)
