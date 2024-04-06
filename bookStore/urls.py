from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # Import the settings module
from django.conf.urls.static import static  # Import the static function

urlpatterns = [
    path('admin/', admin.site.urls),
    path('store/', include('mainApp.urls')),
    path('categorie/', include('categorie.urls')),
 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
