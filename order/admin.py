from django.contrib import admin

from order.models import Order, Basket, BasketItem, ShippingDetail

admin.site.register([ShippingDetail, ])

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('basket', 'total', 'created_at')
    list_filter = ('basket', 'created_at')
    search_fields = ('basket', )


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('author', 'sub_total', 'created_at')
    list_filter = ('author', 'created_at')
    search_fields = ('author__username', )


@admin.register(BasketItem)
class BasketItemAdmin(admin.ModelAdmin):
    list_display = ('basket', 'productVersion', 'price', 'count', 'created_at')
    list_filter = ('basket', 'created_at')
    search_fields = ('productVersion', )


