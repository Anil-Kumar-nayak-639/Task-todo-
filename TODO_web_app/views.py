from django.shortcuts import render,redirect
from TODO_web_app.models import Tasklist
# Create your views here.
def home(request):
    if request.method == "POST":
        task = request.POST.get('list')
        data=Tasklist(task=task)
        data.save()
    
    obj=Tasklist.objects.all()
    return render(request,'todolist.html',{'obj':obj})
def delete_task(request,id):
    obj = Tasklist.objects.get(pk=id)
    obj.delete()
    #return render(request,'todolist.html')
    return redirect('home')
def completed(request,id):
    obj = Tasklist.objects.get(pk=id)
    obj.done = True
    obj.save()
    #return render(request,'todolist.html')
    return redirect('home')
def pending(request,id):
    obj = Tasklist.objects.get(pk=id)
    obj.done = False
    obj.save()
    return redirect('home')
    