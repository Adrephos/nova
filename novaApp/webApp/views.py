from django.shortcuts import render
from webApp.models import Group,Teacher


# Create your views here.
def base(request):
   return render(request, 'base.html')
def home(request):
   return render(request, 'home.html')

def base(request):
   return render(request, 'base.html')

def student(request):
   return render(request, 'student.html')

def studentSuccess(request):
   return render(request, 'studentSuccess.html')

def teachers(request):
   # teacherSelected = Teacher.objects.first(id_eafit=1)
   # groups = Group.objects.filter(teaacher = teacherSelected)
   # context = {'groups':groups,'teacher':teacherSelected}
   return render(request, 'teacher.html')

