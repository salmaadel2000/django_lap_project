from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from django.http import HttpResponse

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

def add(request):
    return render(request, 'mainApp/add.html')

def details(request, id):
    filtered_books = books.filter(id=id)
    if filtered_books.exists():
        product = filtered_books.first() 
        return render(request, 'mainApp/details.html', context={"product": product})
    else:
        return HttpResponse("Product not found")

def book_add(request):
    if request.method == "POST":
        title = request.POST.get("title")
        no_of_pages = request.POST.get("no_of_pages")
        author = request.POST.get("author")
        price = request.POST.get("price")
        image = request.FILES.get("image")
        print(image)
        book = Book(title=title, no_of_pages=no_of_pages, author=author, price=price, image=image)
        book.save()

        return redirect('index') 
    else:
        return render(request, 'mainApp/add.html')

def book_update(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == "POST":
        title = request.POST.get("title")
        no_of_pages = request.POST.get("no_of_pages")
        author = request.POST.get("author")
        price = request.POST.get("price")
        image = request.FILES.get("image")

        book.title = title
        book.no_of_pages = no_of_pages
        book.author = author
        book.price = price
        if image:
            book.image = image

        book.save()
        global books
        books = Book.objects.all()

        return redirect('index')
    else:
        return render(request, 'mainApp/update.html', {'book': book})
    
def book_delete(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == "POST":
        book.delete()
        global books
        books = Book.objects.all()
        return redirect('index')  
    else:
        return redirect('details', id=id)