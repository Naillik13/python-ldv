from django.apps import apps
from django.contrib import admin
from shopping.models import Product, User, Item


class ItemInline(admin.TabularInline):
    model = Item
    extra = 1


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    filter_horizontal = ('user_permissions', 'groups')
    inlines = (ItemInline,)


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
