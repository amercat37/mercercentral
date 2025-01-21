from django.shortcuts import redirect, get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.views import View
from price_checker.models import GroceryStore
from price_checker.forms import GroceryStoreForm

# Create your views here.
class GroceryStoreListView(View):
    def get(self, request):
        grocery_stores = GroceryStore.objects.all()
        context = {"grocery_stores": grocery_stores}
        return render(request, 'grocery_store_list.html', context)

class GroceryStoreAddView(View):
    def get(self, request):
        form = GroceryStoreForm()
        context = {"form": form}
        return render(request, 'grocery_store_add.html', context)

    def post(self, request):
        form = GroceryStoreForm(request.POST)
        grocery_store_name = request.POST.get('name')
        if form.is_valid():
            try:
                form.save()
                messages.success(request, f"Successfully Added Grocery Store: {grocery_store_name}")
            except Exception as e:
                messages.error(request, f"Exception {e} Adding Grocery Store: {grocery_store_name}")
        else:
            messages.error(request, f"Error Adding Duplicate Grocery Store: {grocery_store_name}")
        # Redirect to self no matter what the outcome to continue adding more categories.
        return HttpResponseRedirect(self.request.path_info)

class GroceryStoreEditView(View):
    def get(self, request, grocery_store_id):
        grocery_store = get_object_or_404(GroceryStore, pk=grocery_store_id)
        form = GroceryStoreForm(instance=grocery_store)
        context = {"form": form, "grocery_store": grocery_store}
        return render(request, 'grocery_store_edit.html', context)

    def post(self, request, grocery_store_id):
        grocery_store = get_object_or_404(GroceryStore, pk=grocery_store_id)
        form = GroceryStoreForm(request.POST, instance=grocery_store)
        context = {"form": form, "grocery_store": grocery_store}
        grocery_store_name = request.POST.get('name')
        if form.is_valid():
            try:
                form.save()
                messages.success(request, f"Successfully Updated Grocery Store: {grocery_store_name}")
                # Redirect back to grocery_store_list if successful.
                return redirect('price_checker:grocery_store_list')
            except Exception as e:
                messages.error(request, f"Exception {e} Adding Grocery Store: {grocery_store_name}")
        else:
            messages.error(request, f"Error Updating Duplicate Grocery Store: {grocery_store_name}")
        # Redirect back to self to continue editing if unsuccessful.
        return render(request, 'grocery_store_edit.html', context)

class GroceryStoreDeleteView(View):
    def get(self, request, grocery_store_id):
        grocery_store = get_object_or_404(GroceryStore, pk=grocery_store_id)
        try:
            grocery_store.delete()
            messages.success(request, f"Successfully Deleted Grocery Store: {grocery_store.name}")
        except Exception as e:
            messages.error(request, f"Exception {e} Deleting Grocery Store: {grocery_store.name}")
        return redirect('price_checker:grocery_store_list')
