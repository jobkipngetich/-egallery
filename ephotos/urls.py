

from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
from django.conf .urls import url,include
from carts.views import cart_home
from products.views import(
   ProductFeaturedListView,
   ProductFeaturedDetailView
   )

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^product/', include('products.urls')),
    url(r'^cart/$', cart_home, name='cart'),
    url(r'^search/', include('search.urls')),
    url(r'^featured/$', ProductFeaturedListView.as_view(), name='featuredlist'),
    url(r'^featured/$', ProductFeaturedListView.as_view(), name='featuredlist'),  
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)