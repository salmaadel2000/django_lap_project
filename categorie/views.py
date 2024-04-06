from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from .forms import CategoryModelForm
from .models import Category
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

# Simple landing page view
def landing(request):
    return HttpResponse("<h1>Welcome to Categories App</h1>")

# Display all categories
def categories_index(request):
    categories = Category.objects.all()
    return render(request, 'categorie/main.html', {'categories': categories})

# Show a single category
def category_show(request, id):
    category = get_object_or_404(Category, id=id)
    return render(request, 'categorie/show.html', {'category': category})

# Create category - class-based view
class CreateCategoryView(View):
    def get(self, request):
        form = CategoryModelForm()
        return render(request, 'categorie/create.html', {'form': form})

    def post(self, request):
        form = CategoryModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirect using a named URL pattern
            return redirect('categorie.main')
        return render(request, 'categorie/create.html', {'form': form})

# Edit a category
def edit_category(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        form = CategoryModelForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categorie.main')
    else:
        form = CategoryModelForm(instance=category)
    return render(request, 'categorie/edit.html', {'form': form, 'category': category})


def delete_category(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        category.delete()
        return redirect('categorie.main')

# Login view with superuser check
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('categorie.main')  # Ensure you have this named URL in your urls.py
        else:
            messages.error(request, "Incorrect username or password.")
            return render(request, 'categorie/index.html')
    else:
        return render(request, 'categorie/index.html')
