from django.contrib import admin

# Register your models here.
from .models import Product,Image,Category


class ProductAdmin(admin.ModelAdmin):
    list_display=('product_id','name','description','price','stock_quantity')
admin.site.register(Product,ProductAdmin)

class ImageAdmin(admin.ModelAdmin):
    list_display=('url'),
admin.site.register(Image,ImageAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display=('name','description')
admin.site.register(Category,CategoryAdmin)
