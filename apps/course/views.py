from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def index(request):
    data= Course.objects.all()
    context = {
        'data':data
    }
    return render(request, 'course/index.html', context)

def addnew(request):
    Course.objects.create(name=request.POST['name'], description=request.POST['description'] )
    return redirect('/')

def destroy(request,id):
    destroy = Course.objects.filter(id=id).delete()
    return redirect('/')
