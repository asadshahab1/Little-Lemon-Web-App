from django.db import models
from django.forms import ModelForm

class Drinks(models.Model):
    drink_name = models.CharField(max_length=200)
    price = models.IntegerField()

class Booking(models.Model):
   first_name = models.CharField(max_length=200)    
   last_name = models.CharField(max_length=200)
   guest_number = models.IntegerField()
   comment = models.CharField(max_length=1000)

   def __str__(self):
      return self.first_name + ' ' + self.last_name

class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField(max_length=1000,default="")
    def __str__(self) -> str:
        return self.name
    