from django.shortcuts import render
from webApp.models import Group,Teacher


# Create your views here.
def home(request):
   return render(request, 'home.html')

def base(request):
   return render(request,"base.hmtl")

def teachers(request,id_profesor):

   teacherSelected = Teacher.objects.first(id_eafit=id_profesor)
   
   groups = Group.objects.filter(teaacher = teacherSelected)

   return render(request)













