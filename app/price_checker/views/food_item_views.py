from django.shortcuts import redirect, get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.views import View
from price_checker.models import FoodItem
from price_checker.forms import FoodItemForm

# Create your views here.
class FoodItemListView(View):
    def get(self, request):
        food_items = FoodItem.objects.all()
        context = {"food_items": food_items}
        return render(request, 'food_item_list.html', context)

class FoodItemAddView(View):
    def get(self, request):
        form = FoodItemForm()
        context = {"form": form}
        return render(request, 'food_item_add.html', context)

    def post(self, request):
        form = FoodItemForm(request.POST)
        food_item_name = request.POST.get('name')
        if form.is_valid():
            try:
                form.save()
                messages.success(request, f"Successfully Added Food Item: {food_item_name}")
            except Exception as e:
                messages.error(request, f"Exception {e} Adding Food Item: {food_item_name}")
        else:
            messages.error(request, f"Error Adding Duplicate Food Item: {food_item_name}")
        # Redirect to self no matter what the outcome to continue adding more categories.
        return HttpResponseRedirect(self.request.path_info)

class FoodItemEditView(View):
    def get(self, request, food_item_id):
        food_item = get_object_or_404(FoodItem, pk=food_item_id)
        form = FoodItemForm(instance=food_item)
        context = {"form": form, "food_item": food_item}
        return render(request, 'food_item_edit.html', context)

    def post(self, request, food_item_id):
        food_item = get_object_or_404(FoodItem, pk=food_item_id)
        form = FoodItemForm(request.POST, instance=food_item)
        context = {"form": form, "food_item": food_item}
        food_item_name = request.POST.get('name')
        if form.is_valid():
            try:
                form.save()
                messages.success(request, f"Successfully Updated Food Item: {food_item_name}")
                # Redirect back to food_item_list if successful.
                return redirect('price_checker:food_item_list')
            except Exception as e:
                messages.error(request, f"Exception {e} Adding Food Item: {food_item_name}")
        else:
            messages.error(request, f"Error Updating Duplicate Food Item: {food_item_name}")
        # Redirect back to self to continue editing if unsuccessful.
        return render(request, 'food_item_edit.html', context)

class FoodItemDeleteView(View):
    def get(self, request, food_item_id):
        food_item = get_object_or_404(FoodItem, pk=food_item_id)
        try:
            food_item.delete()
            messages.success(request, f"Successfully Deleted Food Item: {food_item.name}")
        except Exception as e:
            messages.error(request, f"Exception {e} Deleting Food Item: {food_item.name}")
        return redirect('price_checker:food_item_list')
