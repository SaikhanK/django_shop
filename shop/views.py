from pickle import NONE
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.template import context
from .models import *
from .forms import * 
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def homeUser(request):
    all_items =  shopItem.objects.all()
    return render(request, 'homeUser.html', {'all_items': all_items})
    

def shopHomepage(request):
    all_items =  shopItem.objects.all()
    return render(request, 'home.html', {'all_items': all_items})


def registerPage(request):
    form = CreateRegisterForm()
    if request.method == 'POST':
        form = CreateRegisterForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form' : form}
    return render(request, 'accounts/register.html', context)


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('homeUser')

    return render(request, 'accounts/login.html')


def logoutUser(request):
    logout(request)
    return redirect('home')


def userView(request, username):
    if request.method == "post":
        info = User.objects.get(username = username)
        context = {'info' : info}
        return render(request, 'userView.html', context)

def addCart(request, id):
    item = shopItem.objects.get(id = id) 
    if Cart.objects.filter(id = item.id).exists():
        addAmount(request, id)
        return redirect('home')
    Cart.objects.create(name = item.name, cartImage = item.itemimage, amount = 1, id = item.id, price = item.price)
    return redirect('home')

def cart(request):
    allCartItems = Cart.objects.all()
    return render(request, 'cart.html', {'allCartItems' : allCartItems}) 

def deleteCart(request, id):
    item = Cart.objects.get(id = id)
    item.delete()
    return redirect("cart")

def deleteItem(request, id):
    item = shopItem.objects.get(id = id)
    item.delete()
    return redirect('home')
    
def addAmount(request, id):
    plus = Cart.objects.get(id = id)
    plus.amount = plus.amount + 1
    fixPrice = shopItem.objects.get(id = id)
    rightprice = fixPrice.price
    plus.price = plus.price + rightprice 
    plus.save()
    return redirect('cart')
 
def reduceAmount(request, id):
    minus = Cart.objects.get(id = id)
    if minus.amount == 1:
        minus.delete()
        return redirect('cart')
    minus.amount = minus.amount - 1
    fixPrice = shopItem.objects.get(id = id)
    rightprice = fixPrice.price
    minus.price = minus.price - rightprice 
    minus.save()
    return redirect('cart')

