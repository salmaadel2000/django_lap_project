from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from .models import Book
from .forms import BookForm

books = None

def index(request):
    global books 
    if books is None:
        books = Book.objects.all()
    return render(request, 'mainApp/index.html', context={'books': books})

def about(request):
    return render(request, 'mainApp/about.html')

def contact(request):
    return render(request, 'mainApp/contact.html')

class AddBookView(View):
    def get(self, request):
        form = BookForm()
        return render(request, 'mainApp/add.html', {'form': form})

    def post(self, request):
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'mainApp/add.html', {'form': form})

def details(request, id):
    filtered_books = books.filter(id=id)
    if filtered_books.exists():
        product = filtered_books.first() 
        return render(request, 'mainApp/details.html', context={"product": product})
    else:
        return HttpResponse("Product not found")

def book_update(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            global books
            books = Book.objects.all()
            return redirect('index')
    else:
        form = BookForm(instance=book)
    return render(request, 'mainApp/update.html', {'form': form})

def book_delete(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == "POST":
        book.delete()
        global books
        books = Book.objects.all()
        return redirect('index')  
    else:
        return redirect('details', id=id)

class CreateBookView(View):
    def get(self, request):
        form = BookForm()
        return render(request, 'mainApp/add.html', {'form': form})

    def post(self, request):
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'mainApp/add.html', {'form': form})
from django.shortcuts import render


