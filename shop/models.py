from django.db import models
from datetime import date
from django import forms

from django.db.models.fields.files import default_storage


# Create your models here.
class Item(models.Model):
    created_at = models.DateField(default=date.today)   


class shopItem(models.Model):
    name = models.CharField(max_length=200)
    itemimage = models.ImageField(null = True, blank=True)
    price = models.PositiveSmallIntegerField(null=False, blank=False)

class Cart(models.Model):
    name = models.CharField(max_length=200 )
    amount = models.PositiveSmallIntegerField(null=False, blank=False)
    cartImage =  models.ImageField(null = True, blank= True)
    price = models.PositiveSmallIntegerField(null=False, blank=False)

class Accounts(models.Model):

    username = models.CharField(max_length = 200)
    password = forms.CharField(widget=forms.PasswordInput)
    email = models.EmailField(max_length = 200)
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)


