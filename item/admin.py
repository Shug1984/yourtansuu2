from django.contrib import admin
from .models import Item, Closet

@admin.register(Item)
class Itemadmin(admin.ModelAdmin):
    list_display = ('pk','item_name')

#admin.site.register(Item)



admin.site.register(Closet)





# Register your models here.
