from django.db import models
from categorie.models import Category
class Book(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    no_of_pages = models.IntegerField()
    author = models.CharField(max_length=100, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='books/images', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name="books")

    @property
    def image_url(self):
        return f"/media/{self.image}"