from django.contrib import admin

from Market.models import Order, OrderDetail, Product, Store


class OrdersAdmin(admin.ModelAdmin):
    pass


class OrderDetailsAdmin(admin.ModelAdmin):
    pass


class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'description']
    list_editable = ['price', 'description']
    prepopulated_fields = {'slug': ('name',)}


class StoresAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Order, OrdersAdmin)
admin.site.register(OrderDetail, OrderDetailsAdmin)
admin.site.register(Product, ProductsAdmin)
admin.site.register(Store, StoresAdmin)


