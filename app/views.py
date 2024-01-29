from django.shortcuts import render

# Create your views here.
from app.models import *

def equijoin(request):
    EMPObjects=Emp.objects.select_related('deptno').all()
    d={'EMPObjects':EMPObjects}
    return render(request,'equijoin.html',d)