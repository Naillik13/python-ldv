from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from shopping.models import Product


class Index(LoginRequiredMixin, TemplateView):
    """
    Index View
    """

    template_name = "shopping/index.djt.html"

    def get(self, request, *args, **kwargs):
        clothes = Product.objects.all()
        return render(request, self.template_name, {'clothes': clothes})


class Details(TemplateView, LoginRequiredMixin):
    """
    Clothe details
    """

    template_name = "shopping/details.djt.html"

    def get(self, request, *args, **kwargs):
        product = get_object_or_404(Product, id=kwargs['id'])
        user = request.user
        user.products.add(product)
        user.save()
        return render(request, self.template_name, {'product': product})
