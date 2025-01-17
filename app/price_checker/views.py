from django.shortcuts import redirect, get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.views import View
from price_checker.models import FoodCategory
from price_checker.forms import FoodCategoryForm

# Create your views here.
class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

class FoodCategoryListView(View):
    def get(self, request):
        food_categories = FoodCategory.objects.all()
        context = {"food_categories": food_categories}
        return render(request, 'food_category_list.html', context)

class FoodCategoryAddView(View):
    def get(self, request):
        form = FoodCategoryForm()
        context = {"form": form}
        return render(request, 'food_category_add.html', context)

    def post(self, request):
        form = FoodCategoryForm(request.POST)
        food_category_name = request.POST.get('name')
        if form.is_valid():
            try:
                form.save()
                messages.success(request, f"Successfully Added Food Category: {food_category_name}")
            except Exception as e:
                messages.error(request, f"Exception {e} Adding Food Category: {food_category_name}")
        else:
            messages.error(request, f"Error Adding Duplicate Food Category: {food_category_name}")
        # Redirect to self no matter what the outcome to continue adding more categories.
        return HttpResponseRedirect(self.request.path_info)

# Old update method using web form.  Now uses edit view with a POST.
#class FoodCategoryEditView(View):
#    def get(self, request, food_category_id):
#        context = {'food_category': food_category}
#        food_category = FoodCategory.objects.get(pk=food_category_id)
#        return render(request, 'food_category_edit.html', context)

class FoodCategoryEditView(View):
    def get(self, request, food_category_id):
        food_category = get_object_or_404(FoodCategory, pk=food_category_id)
        form = FoodCategoryForm(instance=food_category)
        context = {"form": form, "food_category": food_category}
        return render(request, 'food_category_edit.html', context)

    def post(self, request, food_category_id):
        food_category = get_object_or_404(FoodCategory, pk=food_category_id)
        form = FoodCategoryForm(request.POST, instance=food_category)
        context = {"form": form, "food_category": food_category}
        food_category_name = request.POST.get('name')
        if form.is_valid():
            try:
                form.save()
                messages.success(request, f"Successfully Updated Food Category: {food_category_name}")
                # Redirect back to food_category_list if successful.
                return redirect('price_checker:food_category_list')
            except Exception as e:
                messages.error(request, f"Exception {e} Adding Food Category: {food_category_name}")
        else:
            messages.error(request, f"Error Updating Duplicate Food Category: {food_category_name}")
        # Redirect back to self to continue editing if unsuccessful.
        return render(request, 'food_category_edit.html', context)

# Old update method using web form.  Now uses edit view with a POST.
#class FoodCategoryUpdateView(View):
#    def post(self, request, food_category_id):
#        food_category = get_object_or_404(FoodCategory, pk=food_category_id)
#        form = FoodCategoryForm(request.POST, instance=food_category)
#        food_category_name = request.POST.get('name')
#        if form.is_valid():
#            try:
#                form.save()
#                messages.success(request, f"Successfully Updated Food Category: {food_category_name}")
#                return redirect('price_checker:food_category_list')
#            except Exception as e:
#                messages.error(request, f"Exception {e} Updating Food Category: {food_category_name}")
#        else:
#            messages.error(request, f"Error Updating Duplicate Food Catgory: {food_category_name}")
#        return render(request, 'food_category_edit.html', {'food_category': food_category})

class FoodCategoryDeleteView(View):
    def get(self, request, food_category_id):
        food_category = get_object_or_404(FoodCategory, pk=food_category_id)
        try:
            food_category.delete()
            messages.success(request, f"Successfully Deleted Food Category: {food_category.name}")
        except Exception as e:
            messages.error(request, f"Exception {e} Deleting Food Category: {food_category.name}")
        return redirect('price_checker:food_category_list')
