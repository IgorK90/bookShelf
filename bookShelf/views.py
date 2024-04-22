import string

from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

from bookShelf.models import Author, Book

def index(request:HttpRequest)->HttpResponse:
    return HttpResponse(f"commands examples:<br>"
                        f" http://127.0.0.1:8000/addBook/?name=book1&author=Poirot<br>"
                        f"http://127.0.0.1:8000/delBook/?name=book1<br>"
                        f"http://127.0.0.1:8000/addAuthro/?name=Poirot<br>")

def addAuthor(request:HttpRequest)->HttpResponse:
    author = Author.objects.create(
        #name = "Ivan"
        name = request.GET.get("name")
    )
    author.save()
    return HttpResponse(f"{author.name} is created and saved")

def addBook(request:HttpRequest)->HttpResponse:
    book = Book.objects.create(
        #name = "Suc ve cesa",
        name  = request.GET.get("name"),
        author = Author.objects.create(name = request.GET.get("author"))
        #author = Author.objects.create( name = "Max")
    )
    book.save()
    return HttpResponse(f"Book {book.name} with author {book.author.name} is created and saved")

def delBook(request:HttpRequest, null=None)->HttpResponse:
    #book = Book.objects.filter(name = "Suc ve cesa")
    book = Book.objects.filter(name = request.GET.get("name")).first()
    if book is not null:
        book.delete()
        return HttpResponse(f"Book {book.name} with author {book.author.name} is deleted")
    return  HttpResponse(f"no books are available to delete")