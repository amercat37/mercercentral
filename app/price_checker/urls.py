from django.urls import path
from .views import IndexView
from .views import FoodCategoryListView
from .views import FoodCategoryAddView
from .views import FoodCategoryEditView
#from .views import FoodCategoryUpdateView
from .views import FoodCategoryDeleteView

app_name = 'price_checker'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('food_category_list/', FoodCategoryListView.as_view(), name='food_category_list'),
    path('food_category_add/', FoodCategoryAddView.as_view(), name='food_category_add'),
    path('food_category_edit/<int:food_category_id>', FoodCategoryEditView.as_view(), name='food_category_edit'),
    # Old update method using web form.  Now uses edit view with a POST.
    #path('food_category_update/<int:food_category_id>', FoodCategoryUpdateView.as_view(), name='food_category_update'),
    path('food_category_delete/<int:food_category_id>', FoodCategoryDeleteView.as_view(), name='food_category_delete'),
]
