from django.contrib import admin
from django.urls import path
from mainApp.views import index, about, contact, details, book_update, book_delete, CreateBookView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('add/', CreateBookView.as_view(), name='add'),  
    path('details/<int:id>/', details, name='details'),
    path('update/<int:id>/', book_update, name='update'),
    path('delete/<int:id>/', book_delete, name='delete'),
]
