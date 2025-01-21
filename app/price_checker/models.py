from django.db import models

# Create your models here.
class FoodCategory(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Food Category Name',
                            help_text='General food category name: e.g. "Cheese".')
    description = models.CharField(max_length=100, verbose_name='Description',
                                   blank=True, null=False,
                                   help_text='Food Category description.')

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=3, unique=True, verbose_name='Country Name',
                            help_text='ISO 3166 alpha-2 or alpha-3 country code: e.g. "USA".')
    default_exchange = models.DecimalField(max_digits=5, decimal_places=3, verbose_name='Default Exchange Rate',
                                   help_text='Default exchange rate based on USD: e.g. "1.234".')

    def __str__(self):
        return self.name

class GroceryStore(models.Model):
    name = models.CharField(max_length=50, verbose_name='Grocery Store Name',
                            help_text='Grocery store name: e.g. "Wegmans".')
    location = models.CharField(max_length=75, verbose_name='Location',
                                help_text='Grocery store location: e.g. "123 Amherst Street, Buffalo, NY, 12345".')
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    description = models.CharField(max_length=100, verbose_name='Description',
                                   blank=True, null=False,
                                   help_text='Grocery Store description.')

    class Meta:
        unique_together = ('name', 'location')

    def __str__(self):
        # Return Grocery Store Name + first part of location up to a comma
        return self.name + ' - ' + self.location.split(',')[0]

class FoodSubcategory(models.Model):
    name = models.CharField(max_length=50, verbose_name='Food Subcategory Name',
                            help_text='Food subcategory name: e.g. "Cheddar".')
    parent_category = models.ForeignKey(FoodCategory, on_delete=models.PROTECT)
    description = models.CharField(max_length=100, verbose_name='Description',
                                   blank=True, null=False,
                                   help_text='Food subcategory description.')

    class Meta:
        unique_together = ('name', 'parent_category')

    def __str__(self):
        # Switch to category name and subcategory name.
        return self.name

class FoodItem(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Food Item Name',
                            help_text='Food item name: e.g. "Cabot Creamery Vermont Extra Sharp Chedar Cheese".')
    food_category = models.ForeignKey(FoodCategory, on_delete=models.PROTECT)
    food_subcategory = models.ForeignKey(FoodSubcategory, on_delete=models.PROTECT)
    description = models.CharField(max_length=100, verbose_name='Description',
                                   blank=True, null=False,
                                   help_text='Food item description.')

    def __str__(self):
        return self.name
