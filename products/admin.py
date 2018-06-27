
from django.contrib import admin
from .models import Album, Product

class AlbumAdmin(admin.ModelAdmin):

    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

    class Meta:
        model=Album

admin.site.register(Album, AlbumAdmin)

class ProductAdmin(admin.ModelAdmin):

    list_display = ['__str__', 'slug', 'album','price','available', 'created', 'updated']
    list_filter = ['album','available', 'created', 'updated']
    list_editable = ['price','available']
    prepopulated_fields = {'slug': ('title',)}

    class Meta:
        model=Product

admin.site.register(Product, ProductAdmin)
