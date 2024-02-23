from django.contrib import admin

from .models import Client, Product, Order, OrderStatus


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'address', 'date_reg']
    ordering = ['date_reg']
    list_filter = ['address', 'date_reg']
    search_fields = ['phone', 'address']
    search_help_text = 'Поиск по полю phone и address'


@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'date_add']
    ordering = ['name']
    list_filter = ['date_add']
    search_fields = ['name']
    search_help_text = 'Поиск по полю name'
    actions = [reset_quantity]
    fieldsets = [(None, {'fields': ['name']}),
                 ('описание товара', {'classes': ['collapse'], 'fields': ['description']}),
                 ('склад', {'fields': ['price', 'quantity', 'date_add']})
                 ]
    readonly_fields = ['date_add']


class TermInlineAdmin(admin.TabularInline):
    model = Order.product.through


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'get_total_amount', 'status', 'get_products', 'date_order']
    list_filter = ['status']
    search_fields = ['client__name']
    search_help_text = 'Поиск по полю client'
    fields = ['client', 'status', 'get_total_amount', 'date_order']
    readonly_fields = ['client', 'get_total_amount', 'date_order']
    inlines = (TermInlineAdmin,)


@admin.register(OrderStatus)
class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'status_name']
    list_display_links = ['status_name']

