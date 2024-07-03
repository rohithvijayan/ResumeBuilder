from django.shortcuts import render,redirect,HttpResponse
from .forms import resumeForm
from .models import resume
# Create your views here.
def home(request):
    return render(request,"home.html")
def resume(request):
    return render(request,'resume.html')

def builder(request):
    form=resumeForm()
    if request.method=="POST":
        form=resumeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')     
    context={'form':form}
    return render(request,"builderForm.html",context)