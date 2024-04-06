
from .views import landing
from django.urls import path
from .views import categories_index, category_show, CreateCategoryView, login_view, edit_category, delete_category
# include categories urls
urlpatterns = [

    path('cats', landing, name='categorie'),
    path('create', CreateCategoryView.as_view(), name='categorie.create'),
    path('main', categories_index, name='categorie.main'),
     path('', login_view, name='login'),
    path('<int:id>', category_show, name='categorie.show'),
    path('edit/<int:id>', edit_category, name='edit'),
   path('delete/<int:id>', delete_category, name='delete_category'),

]