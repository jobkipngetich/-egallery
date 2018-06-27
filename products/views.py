
from django.shortcuts import render, get_object_or_404
from django.views.generic  import ListView,DetailView
from .models import Album,Product

def ProductListView(request, album_slug=None):
    album = None
    albums = Album.objects.all()
    products = Product.objects.filter(available=True)
    if album_slug:
      album = get_object_or_404(Album, slug=album_slug)
      products = products.filter(album=album)
    return render(request,
      'product/product_list.html',
      {'album': album,
      'albums': albums,
                'products': products})

def AlbumListView(request, album_slug=None):
    album = None
    albums = Album.objects.all()

    return render(request,
      'product/product-album.html',
      {'album': album,
      'albums': albums})    

class ProductSlugDetailView (DetailView):
    queryset       = Product.objects.all() 
    template_name  ="product/product_detail.html"

class ProductFeaturedListView (ListView): 
    template_name  ="product/product_list.html"

    def get_queryset(self, *args, **kwargs):
      request = self.request
      return Product.objects.all().featured()

class ProductFeaturedDetailView(DetailView):
    queryset       = Product.objects.all().featured() 
    template_name  ="product/featured_detail.html"

    





#def ProductDetailView (request, pk=None,*args, **kwargs):  
# 
 #   instance =Product.objects.get_by_id(pk)
 #   if instance is None: 
 #       raise Http404("Product doesn't exist")
  #  context = {
  #      'object':instance 
  #      }
  #  return render(request,"product/product_detail.html",context)
       

    #qs       = Product.objects.filter (id=pk) 
    #if qs.exists() and qs.count() == 1:
    #   instance = qs.first()
    #else:
    #   raise Http404("Product doesn't exist")
    #instance = get_object_or_404(Product,pk=pk)

    