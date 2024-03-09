from django.contrib import admin
#Or else use from . models import Category 
#Or else use from . models import Product 
from . models import * 
# this will directly import all the models

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','image','description')

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product)