from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q

def equijoin(request):
    EMPObjects=Emp.objects.select_related('deptno').all() #select_related will join the two tables and then retrive the data
    EMPObjects=Emp.objects.select_related('deptno').filter(ename__startswith='B') #by using Fieldlookups we can acheive the condiitions
    EMPObjects=Emp.objects.select_related('deptno').order_by(Length('ename'))
    EMPObjects=Emp.objects.select_related('deptno')


    d={'EMPObjects':EMPObjects}
    return render(request,'equijoin.html',d)


def selfjoin(request):
    Empmgrobj=Emp.objects.select_related('mgr').all() #while selfjoin we use the same table so the common column here is mgr for manageremp table
    Empmgrobj=Emp.objects.select_related('mgr').filter(sal__gt='2500')
    Empmgrobj=Emp.objects.select_related('mgr').filter(mgr__ename='KING')
    Empmgrobj=Emp.objects.select_related('mgr').filter(job='ANALYST')
    Empmgrobj=Emp.objects.select_related('mgr').filter(deptno='10')
    d={'Empmgrobj':Empmgrobj}
    return render(request,'selfjoin.html',d)



def emp_dept_mgr(request):
    emd=Emp.objects.select_related('deptno','mgr').all()
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='BLAKE')
    emd=Emp.objects.select_related('deptno','mgr').filter(sal__gte='1500')
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dloc='NEW YORK')
    emd=Emp.objects.select_related('deptno','mgr').filter(sal__lte='1500',ename__contains='A')
    emd=Emp.objects.select_related('deptno','mgr').all()
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='JONES')
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(deptno__dloc='CHICAGO') | Q(ename='MARTIN'))
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='ACCOUNTING')
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='SALES',mgr__ename='BLAKE')
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(sal__lte='1000') | Q(deptno__dname='RESEARCH'))
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='FORD')
    emd=Emp.objects.select_related('deptno','mgr').filter(ename='ADAMS')
    emd=Emp.objects.select_related('deptno','mgr').filter(job='CLERK')
    emd=Emp.objects.select_related('deptno','mgr').filter(job='ANALYST',sal__gt='1500')
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(ename='TURNER') | Q(job='SALESMAN'))
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='SCOTT',sal__gte='1000')
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno=10,ename__contains='L')
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='KING')
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(job='PRESIDENT') | Q(deptno__dloc='CHICAGO'))
    emd=Emp.objects.select_related('deptno','mgr').filter(ename__startswith='S')
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno=20,comm__isnull=True)
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='KING',comm__isnull=True)
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='CLARK',comm__isnull=True,deptno__dloc='NEW YORK')
    emd=Emp.objects.select_related('deptno','mgr').filter(empno=7902,sal__gt='1500')
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(ename__endswith='S') | Q(deptno__dloc='DALLAS'))
    emd=Emp.objects.select_related('deptno','mgr').filter(ename__startswith='M')
    emd=Emp.objects.select_related('deptno','mgr').filter(sal__gte='3000',deptno__dname='RESEARCH')
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='JONES',sal__gt='1500')
    
    
    d={'emd':emd}
    return render(request,'emp_dept_mgr.html',d)




def emp_salgrade(request):
    EO=Emp.objects.all()
    SO=Salgrade.objects.all()
    #Retriving data whose grade is 3
    SO=Salgrade.objects.filter(grade=3)
    EO=Emp.objects.filter(sal__range=(SO[0].losal,SO[0].hisal)) #grade 3 is only one object so we'll perform indexing to get object

    #Retriving the data whose grade is 3 and 4
    SO=Salgrade.objects.filter(grade__in=(3,4))
    EO=Emp.objects.none() #created empty Queryset to perform concatination
    #we will run for-loop becoz there are more than one object in the list 
    for sgo in SO:
        EO=EO | Emp.objects.filter(sal__range=(sgo.losal,sgo.hisal),ename='BLAKE') #concatinated with the empty Query-set first it will take grade-3 object and then again for loop will run and it takes grade-4 object

    EO=Emp.objects.filter(sal=5000)
    SO=Salgrade.objects.all()
    
    EO=Emp.objects.filter(ename__endswith='R')
    SO=Salgrade.objects.all()

    EO=Emp.objects.all()[3:8]
    SO=Salgrade.objects.all()
    #EO=Emp.objects.all()

    d={'EO':EO,'SO':SO}
    return render(request,'emp_salgrade.html',d)