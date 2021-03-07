from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.core.files.storage import FileSystemStorage
from DjangoHindiApp.models import Notes
from django.contrib.auth.decorators import login_required

# Create your views here.
def demoPage(request):
    return HttpResponse("Simple Demo Page in Django")

def demoPage2(request):
    return render(request,"demoPage1.html")

def loginUser(request):
    if request.user!=None:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("home"))
    return render(request,"login.html")

def signupUser(request):
    return render(request,"signup.html")

def signup_process(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    email=request.POST.get("email")
    first_name=request.POST.get("first_name")
    last_name=request.POST.get("last_name")

    if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
        user=User.objects.create(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
        user.set_password(password)
        user.save()
        messages.success(request,"Signup Successfull")
    else:
        messages.error(request,"Username or Email Already Exist")
    
    return HttpResponseRedirect(reverse("signup"))

def login_proces(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    user=authenticate(username=username,password=password)

    if user!=None:
        login(request,user)
        #messages.success(request,"Login Successfull")
        return HttpResponseRedirect(reverse("home"))
    else:
        messages.error(request,"Invalid Login Details")
        return HttpResponseRedirect(reverse("login"))

@login_required(login_url="/")  
def home(request):
    #return HttpResponse("Home Page Welcome : "+request.user.username+ " ID : "+str(request.user.id)+" FIRST NAME "+request.user.first_name)
    #Example of How to Read Data from Database Multiple and Pass Data to Template
    all_tasks=Notes.objects.filter(user_id=request.user.id)
    return render(request,"home.html",{"all_tasks":all_tasks})

def logoutUser(request):
    logout(request)
    request.user=None
    messages.error(request,"Logout Successfully")
    return HttpResponseRedirect(reverse("login"))

@login_required(login_url="/")    
def add_tasks(request):
    title=request.POST.get("title")
    task=request.POST.get("task")
    thumbnail=request.FILES["thumbnail"]

    fs=FileSystemStorage()
    thumbnail_path=fs.save(thumbnail.name,thumbnail)

    #Fetch Single Data .get() for single Data .filter() for multiple data
    current_user=User.objects.get(id=request.user.id)

    #Use to Save Note Data First Pass Data then Save Data
    note=Notes(title=title,notes_data=task,user_id=current_user,thumbnail=thumbnail_path)
    note.save()
    messages.success(request,"Task Added")
    return HttpResponseRedirect(reverse("home"))

@login_required(login_url="/")
def delete_task(request,id):
    #for single fetch you need to use .get()
    task=Notes.objects.get(id=id)
    task.delete()
    messages.success(request,"Task Deleted")
    return HttpResponseRedirect(reverse("home"))

@login_required(login_url="/")
def edit_task(request,id):

    #Fetching Single Task By ID SO Using .get()
    task=Notes.objects.get(id=id)
    return render(request,"edit_task.html",{"task":task})

@login_required(login_url="/")
def edit_tasks_save(request,id):
    title=request.POST.get("title")
    task_data=request.POST.get("task")

    #Update Data in Model
    task=Notes.objects.get(id=id)
    task.title=title
    task.notes_data=task_data
    task.save()
    messages.success(request,"Data Updated")
    return HttpResponseRedirect(reverse("edit_task",kwargs={"id":id}))