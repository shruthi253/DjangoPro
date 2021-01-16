from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):

    dest = Destination()
    dest.name = 'Germany'
    dest.image = 'destination_1.jpg'
    dest.desc = 'i am coming'
    dest.price = 700
    dest.offer = True

    dest1 = Destination()
    dest1.name = 'Austria'
    dest1.image = 'destination_2.jpg'
    dest1.desc = 'i am coming'
    dest1.price = 800
    dest1.offer = False
    
    dest2 = Destination()
    dest2.name = 'Sweden'
    dest2.image = 'destination_3.jpg'
    dest2.desc = 'i am coming'
    dest2.price = 600
    dest2.offer = False

    dests = [ dest, dest1, dest2]

    return render(request ,'index.html',{'dests' : dests})