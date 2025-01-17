from django import forms
from .models import FoodCategory

class FoodCategoryForm(forms.ModelForm):
    class Meta:
        model = FoodCategory
        #fields = "__all__"
        fields = ('name', 'description')
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'description': forms.TextInput(attrs={'class': 'form-control'}),
                   }
