from django import forms
from .models import FoodCategory, Country, GroceryStore, FoodSubcategory, FoodItem

class FoodCategoryForm(forms.ModelForm):
    class Meta:
        model = FoodCategory
        #fields = "__all__"
        fields = ('name', 'description')
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'description': forms.TextInput(attrs={'class': 'form-control'}),
                   }

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        #fields = "__all__"
        fields = ('name', 'default_exchange')
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'default_exchange': forms.TextInput(attrs={'class': 'form-control'}),
                   }

class GroceryStoreForm(forms.ModelForm):
    class Meta:
        model = GroceryStore
        #fields = "__all__"
        fields = ('name', 'location', 'country', 'description')
        #country = forms.ModelChoiceField(queryset=Country.objects.all(), widget=forms.Select(attrs={'class': 'form-control', 'style': 'display:block;'}))
        country = forms.ModelChoiceField(queryset=Country.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'location': forms.TextInput(attrs={'class': 'form-control'}),
                   #'country': forms.TextInput(attrs={'class': 'form-control'}),
                   'description': forms.TextInput(attrs={'class': 'form-control'}),
                   }

class FoodSubcategoryForm(forms.ModelForm):
    class Meta:
        model = FoodSubcategory
        #fields = "__all__"
        fields = ('name', 'parent_category', 'description')
        #country = forms.ModelChoiceField(queryset=Country.objects.all(), widget=forms.Select(attrs={'class': 'form-control', 'style': 'display:block;'}))
        parent_caegory = forms.ModelChoiceField(queryset=FoodCategory.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   #'location': forms.TextInput(attrs={'class': 'form-control'}),
                   #'country': forms.TextInput(attrs={'class': 'form-control'}),
                   'description': forms.TextInput(attrs={'class': 'form-control'}),
                   }

class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        #fields = "__all__"
        fields = ('name', 'food_category', 'food_subcategory', 'description')
        #country = forms.ModelChoiceField(queryset=Country.objects.all(), widget=forms.Select(attrs={'class': 'form-control', 'style': 'display:block;'}))
        food_caegory = forms.ModelChoiceField(queryset=FoodCategory.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
        food_subcaegory = forms.ModelChoiceField(queryset=FoodSubcategory.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   #'location': forms.TextInput(attrs={'class': 'form-control'}),
                   #'country': forms.TextInput(attrs={'class': 'form-control'}),
                   'description': forms.TextInput(attrs={'class': 'form-control'}),
                   }
