from django.db import models

# Create your models here.
class FoodCategory(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Name',
                            help_text='Food Category Name')
    description = models.CharField(max_length=100, unique=False, verbose_name='Description',
                                   blank=True, null=False,
                                   help_text='Food Category Description')

    def __str__(self):
        return self.name
