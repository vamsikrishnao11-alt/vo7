from django.shortcuts import render
from app1.models import *
# Create your views here.
def poojitha(request):
    a=Dept.objects.all()
    b=Student.objects.all()
    c=Fees.objects.all()
    d={'dept':a,'std':b,'fee':c}
    return render(request,'h1.html',d)