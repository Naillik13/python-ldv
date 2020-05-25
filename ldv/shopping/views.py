from django.shortcuts import render
from django.views.generic.base import TemplateView


class Index(TemplateView):
    """
    Index View
    """

    template_name = "shopping/index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'test': 42})
