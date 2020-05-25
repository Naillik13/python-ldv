from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView

from shopping.models import Clothe


class Index(TemplateView):
    """
    Index View
    """

    template_name = "shopping/index.html"

    def get(self, request, *args, **kwargs):
        clothes = Clothe.objects.all()
        return render(request, self.template_name, {'clothes': clothes})


class Details(TemplateView):
    """
    Clothe details
    """

    template_name = "shopping/details.html"

    def get(self, request, id, *args, **kwargs):
        clothe = get_object_or_404(Clothe, id=id)
        return render(request, self.template_name, {'clothe': clothe})
