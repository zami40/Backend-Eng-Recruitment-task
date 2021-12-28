from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Mobile(models.Model):
    brand_name = models.CharField(max_length=200)
    model_name = models.CharField(max_length=200) 
    color = models.CharField(max_length=200)
    jan_code = models.IntegerField(null=False,unique=True)
    image =  models.ImageField(default='smartphone-icon-logo.png', null=True, blank=True) 

    def __str__(self):
        return self.model_name

    class Meta:
        ordering = ["brand_name"]    