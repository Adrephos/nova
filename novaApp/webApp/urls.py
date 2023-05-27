from django.urls import path
from .views import *

urlpatterns = [
<<<<<<< HEAD
    path('', index, name='index'),
    
=======
    path('', home, name='home'),
    path('base/', base, name='base'),
>>>>>>> origin
]
