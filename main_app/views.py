from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Cat
# class Cat:
#     def __init__(self, name, breed, description, age):
#         self.name = name # self === this from JS
#         self.breed = breed
#         self.description = description
#         self.age = age

# cats = [
#     Cat('Lolo', 'tabby', 'Kinda rude.', 3),
#     Cat('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
#     Cat('Fancy', 'bombay', 'Happy fluff ball.', 4),
#     Cat('Bonk', 'selkirk rex', 'Meows loudly.', 6)
# ]

def home(request):
    return render(request, "home.html") # DTL - Django Template Language # This checks the templates folder

def about(request):
    return render(request, "about.html") # DTL - Django Template Language # This checks the templates folder

def cats_index(request):
    cats = Cat.objects.all()
    return render(request, "cats/index.html", {'cats': cats}) # context is a dictionary
    
def cat_detail(request, cat_id): #cat id is the url parameter of the cats id
    cat = Cat.objects.get(id=cat_id)
    print(cat_id)
    return render(request, "cats/detail.html", {'cat': cat})

class CatCreate(CreateView): # ModelForm
    model = Cat
    fields = "__all__"
    # template_name = "cats/cat_form.html"
    # success_url = "/cats/"

class CatUpdate(UpdateView):
    model = Cat
    fields = ["breed", "description", "age"]

class CatDelete(DeleteView):
    model = Cat
    success_url = "/cats/"

class CatList(ListView):
    model = Cat
    template_name = "cats/index.html"

# class BookCreate(CreateView): # ModelForm
#     model = Book
#     fields = "__all__"

# class BookUpdate(UpdateView):
#     model = Book
#     fields = "__all__"

# class BookDelete(DeleteView):
#     model = Book
#     success_url = "/books/"

# class BookList(ListView):
#     model = Book
#     template_name = "book/index.html"