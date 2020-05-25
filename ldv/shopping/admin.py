from django.apps import apps
from django.contrib import admin
from shopping.models import Clothe


# Register your models here.

@admin.register(Clothe)
class AdminClothe(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    search_fields = ('name', 'price')
    fieldsets = (
        ("Text", {'fields': ('name', 'description')}),
        ("Number", {'fields': ('price',)})
    )


models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
