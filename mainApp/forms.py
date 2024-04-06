from django import forms
from .models import Book, Category

class BookForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False, label='Category', empty_label="Select a Category")

    class Meta:
        model = Book
        fields = ['title', 'no_of_pages', 'author', 'price', 'image', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'no_of_pages': forms.NumberInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }


    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get("category")
        if not category:
            self.add_error('category', "Category field is required.")

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise forms.ValidationError("Title field is required.")
        elif len(title) < 5:
            raise forms.ValidationError("Title must be at least 5 characters long.")
        return title

    def clean_no_of_pages(self):
        no_of_pages = self.cleaned_data.get('no_of_pages')
        if no_of_pages is None:
            raise forms.ValidationError("Number of pages field is required.")
        elif no_of_pages <= 0:
            raise forms.ValidationError("Number of pages must be a positive integer.")
        return no_of_pages

    def clean_author(self):
        author = self.cleaned_data.get('author')
        if not author:
            raise forms.ValidationError("Author field is required.")
        elif len(author) < 3:
            raise forms.ValidationError("Author name must be at least 3 characters long.")
        return author

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is None:
            raise forms.ValidationError("Price field is required.")
        elif price <= 0:
            raise forms.ValidationError("Price must be a positive decimal number.")
        return price
    
    def clean_image(self):
        image = self.cleaned_data.get('image')
        if not image:
            raise forms.ValidationError("Image field is required.")
      
        return image
