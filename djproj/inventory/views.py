from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):

    dests = Destination.objects.all()
    # dest.name = 'DIARY PRODUCTS'
    # dest.image = 'destination_1.jpg'
    # dest.desc = 'Your Protein Intake'
    # dest.price = 700
    # dest.offer = True

    # dest1 = Destination()
    # dest1.name = 'VEGGIES'
    # dest1.image = 'destination_2.jpg'
    # dest1.desc = 'Your herbal Intake'
    # dest1.price = 800
    # dest1.offer = False
    
    # dest2 = Destination()
    # dest2.name = 'CEREALS'
    # dest2.image = 'destination_3.jpg'
    # dest2.desc = 'Your Carbs Intake'
    # dest2.price = 600
    # dest2.offer = False

    # dests = [ dest, dest1, dest2]
    
    return render(request ,'index.html',{'dests' : dests})