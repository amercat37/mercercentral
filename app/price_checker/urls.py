from django.urls import path
from .views import IndexView
from .views import FoodCategoryListView, FoodCategoryAddView, FoodCategoryEditView, FoodCategoryDeleteView
# Edit could be written as a function based view to avoid one line of reduncancy
#from .views import food_category_edit_view
#from .views import FoodCategoryUpdateView
from .views import CountryListView, CountryAddView, CountryEditView, CountryDeleteView
from .views import GroceryStoreListView, GroceryStoreAddView, GroceryStoreEditView, GroceryStoreDeleteView
from .views import FoodSubcategoryListView, FoodSubcategoryAddView, FoodSubcategoryEditView, FoodSubcategoryDeleteView
from .views import FoodItemListView, FoodItemAddView, FoodItemEditView, FoodItemDeleteView

app_name = 'price_checker'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('food_category_list/', FoodCategoryListView.as_view(), name='food_category_list'),
    path('food_category_add/', FoodCategoryAddView.as_view(), name='food_category_add'),
    path('food_category_edit/<int:food_category_id>', FoodCategoryEditView.as_view(), name='food_category_edit'),
    # Edit could be written as a function based view to avoid one line of reduncancy
    #path('food_category_edit/<int:food_category_id>', food_category_edit_view, name='food_category_edit'),
    # Old update method using web form.  Now uses edit view with a POST.
    #path('food_category_update/<int:food_category_id>', FoodCategoryUpdateView.as_view(), name='food_category_update'),
    path('food_category_delete/<int:food_category_id>', FoodCategoryDeleteView.as_view(), name='food_category_delete'),
    path('country_list/', CountryListView.as_view(), name='country_list'),
    path('country/', CountryAddView.as_view(), name='country_add'),
    path('country_edit/<int:country_id>', CountryEditView.as_view(), name='country_edit'),
    path('country_delete/<int:country_id>', CountryDeleteView.as_view(), name='country_delete'),
    path('grocery_store_list/', GroceryStoreListView.as_view(), name='grocery_store_list'),
    path('grocery_store/', GroceryStoreAddView.as_view(), name='grocery_store_add'),
    path('grocery_store_edit/<int:grocery_store_id>', GroceryStoreEditView.as_view(), name='grocery_store_edit'),
    path('grocery_store_delete/<int:grocery_store_id>', GroceryStoreDeleteView.as_view(), name='grocery_store_delete'),
    path('food_subcategory_list/', FoodSubcategoryListView.as_view(), name='food_subcategory_list'),
    path('food_subcategory/', FoodSubcategoryAddView.as_view(), name='food_subcategory_add'),
    path('food_subcategory_edit/<int:food_subcategory_id>', FoodSubcategoryEditView.as_view(), name='food_subcategory_edit'),
    path('food_subcategory_delete/<int:food_subcategory_id>', FoodSubcategoryDeleteView.as_view(), name='food_subcategory_delete'),
    path('food_item_list/', FoodItemListView.as_view(), name='food_item_list'),
    path('food_item/', FoodItemAddView.as_view(), name='food_item_add'),
    path('food_item_edit/<int:food_item_id>', FoodItemEditView.as_view(), name='food_item_edit'),
    path('food_item_delete/<int:food_item_id>', FoodItemDeleteView.as_view(), name='food_item_delete'),
]
