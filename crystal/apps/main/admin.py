# Register your models here.
from django.contrib import admin
from .models import Product, Category, PriceHistory, Promotion

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'categorys', 'time_create', 'price', 'width')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    
    
class PriceHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'price', 'date')
    list_display_links = ('id', 'price', 'date',)
    search_fields = ('id', 'price', 'date',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'time_update')
    list_display_links = ('id', 'title', 'time_create', 'time_update')
    search_fields = ('id', 'title', 'time_create', 'time_update')



class PromotionAdmin(admin.ModelAdmin):
    list_display = ('product', 'description')
    list_display_links = ('product', 'description')
    search_fields = ('product__title', 'description')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(PriceHistory, PriceHistoryAdmin)

admin.site.register(Promotion, PromotionAdmin)
