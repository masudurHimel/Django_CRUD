from django.shortcuts import render, redirect
from django.http import HttpResponse
from User_App.forms import UserForm
from User_App.models import Information
# Create your views here.

def index(request):
    userInformation = Information.objects.order_by('-id')

    if request.method == "POST":
        user_form = UserForm(data = request.POST)
        
        if user_form.is_valid():
            user = user_form.save(commit= False)
            user.set_password(user.password)
            user.save()
            userInformation = Information.objects.order_by('-id')
            return render(request, "index.html", context= {'userInformation' : userInformation})

    return render(request, "index.html",  context= {'userInformation' : userInformation})


def delete(request,id):
    user = Information.objects.get(pk = id)
    user.delete()
    return redirect("/")


def edit(request,id):
    userEdit = Information.objects.get(pk = id)
    userInformation = Information.objects.order_by('-id')
    return render(request, "index.html", context = {'userEdit':userEdit, 'userInformation':userInformation})


def update(request,id):
    x = UserForm(data = request.POST)
    if x.is_valid():
        user = Information.objects.get(pk = id)
        user.email = request.POST['email']
        user.password = request.POST['password']
        user.set_password(user.password)
        user.save()
        return redirect('/')
        

    return redirect('/')

