from django.apps import apps
from django.contrib import admin
from shopping.models import Product


# Register your models here.

@admin.register(Product)
class AdminClothe(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    search_fields = ('name', 'price')
    fieldsets = (
        ("Text", {'fields': ('name', 'description')}),
        ("Number", {'fields': ('price',)}),
        (None, {'fields': ('image',)})
    )


models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
