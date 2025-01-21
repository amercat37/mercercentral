from django.shortcuts import redirect, get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.views import View
from price_checker.models import FoodSubcategory
from price_checker.forms import FoodSubcategoryForm

# Create your views here.
class FoodSubcategoryListView(View):
    def get(self, request):
        food_subcategories = FoodSubcategory.objects.all()
        context = {"food_subcategories": food_subcategories}
        return render(request, 'food_subcategory_list.html', context)

class FoodSubcategoryAddView(View):
    def get(self, request):
        form = FoodSubcategoryForm()
        context = {"form": form}
        return render(request, 'food_subcategory_add.html', context)

    def post(self, request):
        form = FoodSubcategoryForm(request.POST)
        food_subcategory_name = request.POST.get('name')
        if form.is_valid():
            try:
                form.save()
                messages.success(request, f"Successfully Added Food Subcategory: {food_subcategory_name}")
            except Exception as e:
                messages.error(request, f"Exception {e} Adding Food Subcategory: {food_subcategory_name}")
        else:
            messages.error(request, f"Error Adding Duplicate Food Subcategory: {food_subcategory_name}")
        # Redirect to self no matter what the outcome to continue adding more categories.
        return HttpResponseRedirect(self.request.path_info)

class FoodSubcategoryEditView(View):
    def get(self, request, food_subcategory_id):
        food_subcategory = get_object_or_404(FoodSubcategory, pk=food_subcategory_id)
        form = FoodSubcategoryForm(instance=food_subcategory)
        context = {"form": form, "food_subcategory": food_subcategory}
        return render(request, 'food_subcategory_edit.html', context)

    def post(self, request, food_subcategory_id):
        food_subcategory = get_object_or_404(FoodSubcategory, pk=food_subcategory_id)
        form = FoodSubcategoryForm(request.POST, instance=food_subcategory)
        context = {"form": form, "food_subcategory": food_subcategory}
        food_subcategory_name = request.POST.get('name')
        if form.is_valid():
            try:
                form.save()
                messages.success(request, f"Successfully Updated Food Subcategory: {food_subcategory_name}")
                # Redirect back to food_subcategory_list if successful.
                return redirect('price_checker:food_subcategory_list')
            except Exception as e:
                messages.error(request, f"Exception {e} Adding Food Subcategory: {food_subcategory_name}")
        else:
            messages.error(request, f"Error Updating Duplicate Food Subcategory: {food_subcategory_name}")
        # Redirect back to self to continue editing if unsuccessful.
        return render(request, 'food_subcategory_edit.html', context)

class FoodSubcategoryDeleteView(View):
    def get(self, request, food_subcategory_id):
        food_subcategory = get_object_or_404(FoodSubcategory, pk=food_subcategory_id)
        try:
            food_subcategory.delete()
            messages.success(request, f"Successfully Deleted Food Subcategory: {food_subcategory.name}")
        except Exception as e:
            messages.error(request, f"Exception {e} Deleting Food Subcategory: {food_subcategory.name}")
        return redirect('price_checker:food_subcategory_list')
