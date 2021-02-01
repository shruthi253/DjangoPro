from django.urls import path
from . import views

## pathnames to be specified here
## '' or '/' corresponds to home page
## add_num is the form we added and has to be given here
## methds used in urls are defined in views

urlpatterns = [
    path('register', views.register,name='register'),
]