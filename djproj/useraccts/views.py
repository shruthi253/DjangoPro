from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name =  request.POST['last_name']
        user_name = request.POST['user_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        user = User.objects.create_user(first_name=first_name,last_name=last_name,
               username=user_name,email=email,password=password1)
        user.save()
        print('user created')
        return redirect('/')
    else:  
        return render(request,'register.html')