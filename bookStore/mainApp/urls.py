from django.contrib import admin
from django.urls import path
from mainApp.views import index, about, contact, details, book_add,book_update,book_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('add', book_add, name='add'),  
    path('<int:id>/', details, name='details'),
    path('<int:id>/update',book_update,name="update"),
 path('<int:id>/delete/', book_delete, name='delete')
]