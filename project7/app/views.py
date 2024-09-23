from django.shortcuts import render
from .forms import *
from .models import *
from django.http import HttpResponse
# Create your views here.
def register(request):
    EDFO = DataForm()
    d = {'EDFO': EDFO}
    if request.method == 'POST':
        name = request.POST.get('name')
        pno = request.POST.get('pno')
        email = request.POST.get('email')
        add = request.POST.get('add')
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        D = Data(name=name, pno=pno, email=email, add=add, un=un, pw=pw)
        D.save()
        return HttpResponse('Done')
    return render(request, 'register.html', d)