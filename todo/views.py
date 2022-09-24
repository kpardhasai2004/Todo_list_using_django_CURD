from multiprocessing import context
from django.shortcuts import redirect, render, get_object_or_404
from .models import task
from django.urls import reverse

# Create your views here.

def thome(request):
        tasks = task.objects.all()
        return render(request,'thome.html',{'tasks':tasks})

def tupload(request):
    if request.method == 'POST':
        Task=request.POST['task']
        T= task(work=Task)
        T.save()
        return redirect('thome')
    return render(request,'tupload.html')

def tdelete(request, id):
    if request.method == 'POST':
        task.objects.get(id=id).delete()
    return redirect('thome')

def tupdate(request, id):
    if request.method == 'POST':
        ut = request.POST.get('utask',False)
        task.objects.filter(id=id).update(work=ut)
        return render(request,'tupdate.html')
    return redirect('thome')
    
def tcomp(request, id):
    if request.method == 'POST':
        ct = "Task completed"
        task.objects.filter(id=id).update(work=ct)
    return redirect('thome')
