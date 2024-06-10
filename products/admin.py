from django.contrib import admin

# Register your models here.
from products.models import Categories, Products

# admin.site.register(Categories)
# admin.site.register(Products)

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields={'slyg': ('name',)}

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields={'slyg': ('name',)}   
    list_display = ["name", "quntity", "price", "descount"]
    list_editable = ["descount",]
    list_filter = ["descount", "quntity", "category"]