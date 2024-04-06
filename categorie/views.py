from django.shortcuts import render
from django.views import View
from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from .forms import CategoryModelForm
from .models import  Category
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login

def landing(request):
    return HttpResponse("<h1>Welcome to Categories app </h1>")

def categories_index(request):
    categories = Category.objects.all()  # Retrieve all categories from the database
    return render(request, 'categorie/main.html', {'categories': categories})



def category_show(request, id):
    category = Category.get_category_by_id(id)
    return render(request, 'categorie/show.html', {'category' : category})

class CreateCategoryView(View):
    def get(self, request):
        form = CategoryModelForm()
        return render(request, 'categorie/create.html', {'form': form})

    def post(self, request):
        form = CategoryModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('categorie.main')
        return render(request, 'categorie/create.html', {'form': form})


def login_view(request):
      return render(request, 'categorie/index.html')

def edit_category(request, id):
    category = Category.objects.get(id=id)
    if request.method == 'POST':
        form = CategoryModelForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categorie.main') 
    else:
        form = CategoryModelForm(instance=category)
    return render(request, 'categorie/edit.html', {'form': form, 'category': category})



def delete_category(request, id):
    # Retrieve the category object by its ID or return a 404 error if not found
    category = get_object_or_404(Category, id=id)
    
    if request.method == 'POST':
        # If the request method is POST, delete the category and redirect to the categories index page
        category.delete()
        return redirect('categorie.main')
    
    # If the request method is not POST, render a confirmation page to confirm deletion
    return render(request, 'categorie/main.html', {'category': category})
