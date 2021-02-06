from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Items
from inventory.models import Destination

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'User not Found/Invalid Credentials')            
    else:
        return render(request,'login.html')
       
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name =  request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'User already exists')
                print('user exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already exits')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
                user.save()
                messages.info(request,'User created')
                print('user created')
                return redirect('login')
        else:
            messages.info(request,'Password Mismatch')
            return redirect('register')
    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return render(request,'logout.html')

def items(request):
    if request.method == 'POST':
        item_name = request.POST['item_name']
        price = request.POST['price']
        quantity = request.POST['quantity']
        category = request.POST['category']

        # item = Items(item_name=item_name, price=price,quantity=quantity,user_id=ID)
        # item.save()
        request.user.items_set.create(item_name=item_name, price=price,quantity=quantity,category=category)
        return redirect('items')               
    else:
        items_ = Items.objects.all()
        return render(request,'items.html',{'items_' : items_})  


      

