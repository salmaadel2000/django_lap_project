from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),  # Login page
    path('landing/', views.landing, name='landing'),  # Landing page
    path('main/', views.categories_index, name='categorie.main'),  # Main page showing all categories
    path('create/', views.CreateCategoryView.as_view(), name='categorie.create'),  # Page for creating a new category
    path('<int:id>/', views.category_show, name='categorie.show'),  # Detail page for a specific category
    path('edit/<int:id>/', views.edit_category, name='edit'),  # Page for editing an existing category
    path('delete/<int:id>/', views.delete_category, name='delete_category'),  # Route for deleting a category
]