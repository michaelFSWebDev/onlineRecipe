from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User as LoggedUser

# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == "GET":
        return redirect('/')
    errors = LoggedUser.objects.validate(request.POST)
    if len(errors) > 0:
        for er in errors.values():
            messages.error(request, er)
        return redirect('/')
    else:
        new_user = LoggedUser.objects.register(request.POST)
        request.session['user_id'] = new_user.id
        messages.success(request, "You have successfully registered")
        return redirect('/success')

def login(request):
    if request.method == "GET":
        return redirect('/')
    if not LoggedUser.objects.authenticate(request.POST['email'],
        request.POST['password']):
        messages.error(request, "Invalid Email/Password")
        return redirect('/')
    user = LoggedUser.objects.get(email=request.POST['email'])
    request.session['user_id'] = user.id
    messages.success(request, "You have successfully logged in!")
    return redirect('/success')

def logout(request):
    request.session.clear()
    return redirect('/')

def success(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'user' : LoggedUser.objects.get(id=request.session['user_id'])
    }
    # return redirect("recipe:recipe-dashboard/{user_id}")
    return redirect("/recipe")