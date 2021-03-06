
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save


from products.models import Product
from django.contrib.auth import authenticate
User = settings.AUTH_USER_MODEL

class CartManager(models.Manager):
	def new_or_get(self,request):
		cart_id  = request.session.get("cart_id",None)
		qs = self.get_queryset().filter(id=cart_id)
		if qs.count() == 1:
			new_obj = False
			cart_obj = qs.first()
			if request.user.is_authenticated and cart_obj.user is None:
				cart_obj.user = request.user
				cart_obj.save()
		else:
			cart_obj = Cart.objects.create(user=request.user)
			new_obj = True
			request.session["cart_id"]= cart_obj.id		
			return cart_obj, new_obj
			def cart_new(self,user=None):
				user_obj = None
				if user is not None:
					if user.is_authenticated:
						user_obj = user
				return self.model.objects.create(user = user_obj)

class Cart(models.Model):
	user       = models. ForeignKey(User, on_delete=models.PROTECT,null=True,blank=True)
	products   = models. ManyToManyField(Product,blank=True)
	total      = models. DecimalField(default=0.00, max_digits=100, decimal_places=2)
	updated    = models. DateTimeField(auto_now=True)
	timestamp  = models. DateTimeField(auto_now_add=True)

	objects = CartManager()

	def __str__(self):
		return str(self.id)

def pre_save_cart_receiver(sender, instance, *args , **kwargs):
	products = instance.products.all()
	if new_obj is not None:
		total = 0
		for x in products:
			total += x.price
		instance.total = total

pre_save.connect(pre_save_cart_receiver, sender=Cart)
		