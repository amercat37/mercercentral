#!/bin/bash

# You will still need to create a model, create a form, and fix the add, edit, and list templates.

model_replace="FoodCategory"
variable_singular_replace="food_category"
variable_plurl_replace="food_categories"
text_singular_replace="Food Category"
text_plurl_replace="Food Categories"

if [ $# -ne 5 ]; then
  echo "Usage: $0 'model - e.g.: FoodCategory' 'singular variable - e.g.: food_category' 'plurl variable - e.g.: food_categories' 'text singular - e.g.: Food Category' 'text plurl - e.g.: Food Categories'"
  echo "Description: Replace the above with the provided arguments."
  echo 'Example: ./deploy_new_view.sh "FoodCategory" "food_category" "food_categories" "Food Category" "Food Categories"'
  exit 1
fi

# forms.py
echo "Adding $1 model to forms.py import statement:"
(grep -v '^\s*$\|^\s*\#' forms.py | grep -q "from .models import .*, $1" && echo "    Value already exists.") || \
(sed -i "/^from .models import/s/$/, $1/" forms.py && echo "    Value has been modified.")
echo ""

# admin.py
echo "Adding $1 model to admin.py import statement:"
(grep -v '^\s*$\|^\s*\#' admin.py | grep -q "from .models import .*, $1" && echo "    Value already exists.") || \
(sed -i "/^from .models import/s/$/, $1/" admin.py && echo "    Value has been modified.")
echo ""

# admin.py
echo "Adding $1 register statement to admin.py:"
(grep -v '^\s*$\|^\s*\#' admin.py | grep -q "admin.site.register($1)" && echo "    Value already exists.") || \
(echo "admin.site.register($1)" >> admin.py && echo "    Value has been modified.")
echo ""

# views
  echo "Creating file ${2}_views.py from ${variable_singular_replace}_views.py:"
if [[ ! -f "views/${2}_views.py" ]]; then
  cp "views/${variable_singular_replace}_views.py" "views/${2}_views.py"
  sed -i "s/$model_replace/$1/g" "views/${2}_views.py"
  sed -i "s/$variable_singular_replace/$2/g" "views/${2}_views.py"
  sed -i "s/$variable_plurl_replace/$3/g" "views/${2}_views.py"
  sed -i "s/$text_singular_replace/$4/g" "views/${2}_views.py"
  echo "    File has been created"
else
  echo "    File already exists"
fi
echo ""

# views
echo "Adding ${2}_views to views/__inti__.py import statement:"
(grep -v '^\s*$\|^\s*\#' views/__init__.py | grep -q "from .${2}_views import" && echo "    Value already exists.") || \
(echo "from .${2}_views import ${1}ListView, ${1}AddView, ${1}EditView, ${1}DeleteView" >> views/__init__.py && echo "    Value has been modified.")
echo ""

# templates
echo "Creating $2 template files:"
if [[ ! -f "templates/${2}_add.html" ]] && [[ ! -f "templates/${2}_edit.html" ]] && [[ ! -f "templates/${2}_list.html" ]]; then
  cp "templates/${variable_singular_replace}_add.html" "templates/${2}_add.html"
  cp "templates/${variable_singular_replace}_edit.html" "templates/${2}_edit.html"
  cp "templates/${variable_singular_replace}_list.html" "templates/${2}_list.html"
  sed -i "s/$variable_singular_replace/$2/g" "templates/${2}_"*.html
  sed -i "s/$variable_plurl_replace/$3/g" "templates/${2}_"*.html
  sed -i "s/$text_singular_replace/$4/g" "templates/${2}_"*.html
  sed -i "s/$text_plurl_replace/$5/g" "templates/${2}_"*.html
  echo "    Files have been created"
else
  echo "    At least one file already exists"
fi
echo ""

# index.html
echo "Add button to index for $5:"
if ! grep -q ">${5}<" templates/index.html; then
  sed -i "s/{% endblock content %}//" templates/index.html
  truncate -s -1 templates/index.html
  echo '<div class="mb-4 col-md-12 text-center">' >> templates/index.html
  echo "  <span><a href=\"{% url 'price_checker:${2}_list' %}\" class=\"btn btn-primary col-2\">${5}</a></span>" >> templates/index.html
  echo "</div>" >> templates/index.html
  echo "{% endblock content %}" >> templates/index.html
  echo "    Button added to index"
else
  echo "    Button already exists in index"
fi
echo ""

# urls
echo "Adding ${2} to urls import statement:"
(grep -v '^\s*$\|^\s*\#' urls.py | grep -q "from .views import ${1}ListView" && echo "    Value already exists.") || \
(sed -i "0,/^$/s//from .views import ${1}ListView, ${1}AddView, ${1}EditView, ${1}DeleteView\n/" urls.py && echo "    Value has been modified.")
echo ""

echo "Add urls for $2:"
if ! grep -q "${2}_list" urls.py && ! grep -q "${2}_add" urls.py && ! grep -q "${2}_edit" urls.py && ! grep -q "${2}_delete" urls.py; then
    sed -i 's/]//' urls.py
    truncate -s -1 urls.py
    echo "    path('${2}_list/', ${1}ListView.as_view(), name='${2}_list')," >> urls.py
    echo "    path('${2}/', ${1}AddView.as_view(), name='${2}_add')," >> urls.py
    echo "    path('${2}_edit/<int:${2}_id>', ${1}EditView.as_view(), name='${2}_edit')," >> urls.py
    echo "    path('${2}_delete/<int:${2}_id>', ${1}DeleteView.as_view(), name='${2}_delete')," >> urls.py
    echo "]" >> urls.py
  echo "    Urls added to list"
else
  echo "    At least one url already exists in the list"
fi
echo ""
