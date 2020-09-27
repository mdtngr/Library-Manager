from django.db import models

# from django.db.models.signals import (pre_save, post_delete)
# from django.utils.text import slugify
# from django.conf import settings
# from django.dispatch import receiver

# def upload_location(instance, filename, **kwargs):
#     file_path = 'item/{param1}/{param2}'.format( param1 = str(instance.item_id), param2 = str(instance.hsn_code), filename = filename)
#     return file_path

# Create your models here.

class Categories(models.Model):
    category_id     = models.IntegerField(primary_key=True) 
    category_name   = models.CharField(null =False, blank =False, max_length = 15)


class ItemDetails(models.Model):
    item_id             = models.IntegerField(primary_key=True, null=False, auto_created=True)
    item_name           = models.CharField(null=False, blank=False, max_length=50)
    hsn_code            = models.CharField(null=False, blank=False, max_length=20)
    publisher           = models.CharField(default="NULL", max_length=30)
    shelf               = models.CharField(default="NULL", max_length=30)
    item_quantity       = models.IntegerField(default=0,null = False)
    author              = models.CharField(default="Unknown", max_length=30)
    item_category       = models.CharField(default='None', max_length=15)
    item_quantity       = models.IntegerField(default=0, null=False)
    item_image          = models.ImageField(upload_to='static_cdn/img', null = True, blank= True)
    
    def __str__(self):
        return self.item_name



        