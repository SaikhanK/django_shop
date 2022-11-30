from django.contrib.auth.models import UnicodeUsernameValidator
from django.urls import path
from .views import *
from django.urls import path, include


urlpatterns = [
    path("", shopHomepage, name='home'),
    path("homeUser/", homeUser, name ='homeUser'),
    path("logout/", logoutUser, name = 'logout'),
    path("cart/", cart, name='cart'),
    path("delete/<int:id>", deleteItem, name = 'delete'),
    path("addCartI/<int:id>", addCart, name = 'addCartItem'),
    path("userView", userView, name = 'userView'),
    path('deleteCart/<int:id>', deleteCart, name = 'deleteCart'),
    path("addAmount/<int:id>", addAmount, name = 'addAmount'),
    path("reduceAmount/<int:id>", reduceAmount, name = 'reduceAmount'),
    path("registerPage/", registerPage, name = 'register'),
    path("loginPage/", loginPage, name = 'login'),
]

