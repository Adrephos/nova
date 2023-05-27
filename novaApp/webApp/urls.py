from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('base/', base, name='base'),
    path('student/', student, name='student'),
    path('student/success', studentSuccess, name='studentSuccess')
]