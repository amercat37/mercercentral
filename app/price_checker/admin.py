from django.contrib import admin
from .models import FoodCategory, Country, GroceryStore, FoodSubcategory, FoodItem

# Register your models here.
admin.site.register(FoodCategory)
admin.site.register(Country)
admin.site.register(GroceryStore)
admin.site.register(FoodSubcategory)
admin.site.register(FoodItem)
