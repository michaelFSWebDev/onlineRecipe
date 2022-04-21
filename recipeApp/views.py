from django.shortcuts import render, redirect
from userApp.models import User as LoggedUser


# Create your views here.
def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = LoggedUser.objects.get(id=request.session['user_id'])
    context = {
        'user' : user
    }
    return render (request, 'dashboard.html', context )


def addForm(request):
    return render(request, 'addForm.html')

def recipeDetails(request, r_id):
    context ={

    }
    return render(request,'showRecipe.html', context)

def updateForm(request, r_id):
    context = {

    }
    return render(request,'updateForm.html', context)

def createRecipe(request):
    pass

def updateRecipe(request):
    # return redirect('recipe:recipe-details')
    pass

def deleteRecipe(request):
    pass