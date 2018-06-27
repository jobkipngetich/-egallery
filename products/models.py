
import random
import os 
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save
from django.urls import reverse  
from .utils import unique_slug_generator

def get_filename_ext(filepath):

    base_name=os.path.basename(filepath)
    name,ext=os.path.splitext(base_name)
    return name,ext

def upload_image_path(instance,filename):

    new_filename=random.randint(1,3910209312)
    name,ext=get_filename_ext(filename)
    final_filename='{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)
    return "products/{new_filename}/{final_filename}".format(
        new_filename=new_filename,
        final_filename=final_filename
        )

class ProductQuerySet(models.query.QuerySet):

    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True)

    def search(self,query):
        lookups = (Q(title__icontains=query) |
                   Q(caption__icontains=query) |
                   Q(price__icontains=query) |
                  Q(tag__title__icontains=query)
                  )
        return self.filter(lookups).distinct() 

class ProductManager(models.Manager):

    def get_queryset(self):
        return ProductQuerySet(self.model,using=self._db)

    def all(self):
        return self.get_queryset().active()

    def features(self):
        return self.get_queryset().featured()

    def get_by_id(self,id):
        qs=self.get_queryset().filter(id=id)
        if qs.count()==1:
            return qs.first()
        return None
    
    def search(self,query): 
        return self.get_queryset().active().search(query)

class Album(models.Model):

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,unique=True)
    image        = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('product:product_list_by_album',args=[self.slug])

    class Meta:
        ordering = ('title',)
        verbose_name = 'album'
        verbose_name_plural = 'albums'

    def __str__(self):
        return self.title

class Product(models.Model):
    album        = models.ForeignKey(Album,on_delete=models.PROTECT,default=1,related_name='products')
    title        = models.CharField(max_length=120)
    slug         = models.SlugField(blank=True, unique=True)
    caption      = models.TextField()
    price        = models.DecimalField(decimal_places=2,max_digits=10,default=999.99)
    image        = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    featured     = models.BooleanField(default=False)
    active       = models.BooleanField(default=True)
    timestamp    = models.DateField(auto_now_add=True)
    available    = models.BooleanField(default=True)
    created      = models.DateTimeField(auto_now_add=True)
    updated      = models.DateTimeField(auto_now=True)


    objects     =ProductManager()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return "/products/{slug}/".format(slug=self.slug)
  
    def product_pre_save_receiver(sender, instance, *args , **kwargs):

        if not instance.slug:
            instance.slug = 'abc'      
            pre_save.connect(product_pre_save_receiver, sender=Product)













