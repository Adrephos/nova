from django.shortcuts import render
import models

# Create your views here.
def home(request):
   return render(request, 'home.html')






