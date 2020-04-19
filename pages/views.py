from django.shortcuts import render
from .models import Post


def main_page(request):
    return render(request,'main.html')



def about(request):
    with open ('pages/about.txt', 'r') as file:
        data = file.read()
    return render(request,'about.html', {'data': data})

def contacts(request):
    with open('pages/contacts.txt', 'r') as file:
        contact = file.read()
    return render (request,'contacts.html',{'contact': contact})

def gallery(request):
    post = Post.objects.all()
    return render(request,'galery.html',{"post": post})






    
    
