
from django.conf .urls import url

from products.views import(
	AlbumListView,
   ProductListView,
   ProductSlugDetailView,
   )
app_name='product'

urlpatterns = [
    url(r'^$', AlbumListView, name='album_list'),
    url(r'^all$',  ProductListView, name='product_list'),
    url(r'^(?P<album_slug>[-\w]+)/$',ProductListView,name='product_list_by_album'),
    url(r'^(?P<slug>[\w-]+)/$', ProductSlugDetailView.as_view(), name='detail')
]
  