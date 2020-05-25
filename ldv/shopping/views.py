from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from shopping.models import Product, Item


class Index(LoginRequiredMixin, TemplateView):
    """
    Index View
    """

    template_name = "shopping/shop.djt.html"

    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        return render(request, self.template_name, {'products': products})


class Details(TemplateView, LoginRequiredMixin):
    """
    Clothe details
    """

    template_name = "shopping/details.djt.html"

    def get(self, request, *args, **kwargs):
        product = get_object_or_404(Product, id=kwargs['id'])
        Item.objects.create(user=request.user, product=product)
        return render(request, self.template_name, {'product': product})


class Cart(TemplateView, LoginRequiredMixin):
    """
    User cart
    """

    template_name = "shopping/cart.djt.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'items': request.user.items.all()})
