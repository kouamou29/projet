from django.contrib.auth.models import User
from  django.contrib.auth  import authenticate , login 
from django.shortcuts import render, get_object_or_404
from datetime import date 
from . models import Produts, Category
from django.core.paginator import Paginator

# Create your views here.

def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
   
    user = authenticate(request, username= username, password=password)
    context= {'user':user}
    if user is not None:
        if user.is_active:
            login(request , user )
    
    return render(request, 'accont/login.html', context)

def index(request, ):
    produt = Produts.objects.all()
    item_name = request.GET.get('item_name')
    if item_name !='' and  item_name is not None :
        produt = produt.filter(tilte__icontains=item_name)
    

    paginator = Paginator(produt, 4)
    page_number = request.GET.get('page')
    pag_obj = paginator.get_page(page_number)
    context = {'produt': produt , 'pag_obj':pag_obj}
    
    return render(request, 'blog/index.html', context)


def category(request):
  
  return render(request, 'blog/category.html')

#detail of product page 
def detail(request,pk):
    produt= Produts.objects.get(id=pk)
    return render(request, 'blog/detail.html', {'produt':produt})  
    
def about(request):
  
    return render(request, 'blog/about.html')

  
    

