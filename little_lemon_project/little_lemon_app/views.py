from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu
from .forms import BookingForm
# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def booking(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'booking.html', context)

def menu(request):
    menu_items = Menu.objects.all()
    item_dict = {"menu":menu_items}
    print(menu_items)
    return render(request,'menu.html',item_dict)

def display_menu_items(request,pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ""
    return render(request,"menu_item.html",{"menu_item":menu_item})
def contact(request):
    return HttpResponse("<h2>Contact us</h2>")

def drinks(request,drink_name):
    drink = {
        "mocha":"type of coffee",
        "milk": "type of hot beverage",
    }
    choice_of_drink = drink[drink_name]
    return HttpResponse(f"<h1>{drink_name}</h1>")