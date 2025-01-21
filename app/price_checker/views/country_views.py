from django.shortcuts import redirect, get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.views import View
from price_checker.models import Country
from price_checker.forms import CountryForm

# Create your views here.
class CountryListView(View):
    def get(self, request):
        countries = Country.objects.all()
        context = {"countries": countries}
        return render(request, 'country_list.html', context)

class CountryAddView(View):
    def get(self, request):
        form = CountryForm()
        context = {"form": form}
        return render(request, 'country_add.html', context)

    def post(self, request):
        form = CountryForm(request.POST)
        country_name = request.POST.get('name')
        if form.is_valid():
            try:
                form.save()
                messages.success(request, f"Successfully Added Country: {country_name}")
            except Exception as e:
                messages.error(request, f"Exception {e} Adding Country: {country_name}")
        else:
            messages.error(request, f"Error Adding Duplicate Country: {country_name}")
        # Redirect to self no matter what the outcome to continue adding more categories.
        return HttpResponseRedirect(self.request.path_info)

class CountryEditView(View):
    def get(self, request, country_id):
        country = get_object_or_404(Country, pk=country_id)
        form = CountryForm(instance=country)
        context = {"form": form, "country": country}
        return render(request, 'country_edit.html', context)

    def post(self, request, country_id):
        country = get_object_or_404(Country, pk=country_id)
        form = CountryForm(request.POST, instance=country)
        context = {"form": form, "country": country}
        country_name = request.POST.get('name')
        if form.is_valid():
            try:
                form.save()
                messages.success(request, f"Successfully Updated Country: {country_name}")
                # Redirect back to country_list if successful.
                return redirect('price_checker:country_list')
            except Exception as e:
                messages.error(request, f"Exception {e} Adding Country: {country_name}")
        else:
            messages.error(request, f"Error Updating Duplicate Country: {country_name}")
        # Redirect back to self to continue editing if unsuccessful.
        return render(request, 'country_edit.html', context)

class CountryDeleteView(View):
    def get(self, request, country_id):
        country = get_object_or_404(Country, pk=country_id)
        try:
            country.delete()
            messages.success(request, f"Successfully Deleted Country: {country.name}")
        except Exception as e:
            messages.error(request, f"Exception {e} Deleting Country: {country.name}")
        return redirect('price_checker:country_list')
