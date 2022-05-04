from django.shortcuts import render, redirect
from .models import Recipe as Recipe_id
from userApp.models import User as LoggedUser


# Create your views here.
def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = LoggedUser.objects.get(id=request.session['user_id'])
    context = {
        'user' : user,
        'recipe': Recipe_id.objects.all()
    }
    return render (request, 'dashboard.html', context )


def addForm(request):
    user = LoggedUser.objects.get(id=request.session['user_id'])

    context = {
    'user' : user
}
    return render(request, 'addForm.html', context)

def recipeDetails(request, recipe_id):
    
    context ={
        'oneRecipe' : Recipe_id.objects.get(id=recipe_id)
    }
    return render(request,'showRecipe.html', context)

def updateForm(request, recipe_id):
    
    context = {

    }
    return render(request,'updateForm.html', context)

def createRecipe(request):
    user = LoggedUser.objects.get(id=request.session['user_id'])
    recipe = Recipe_id.objects.create(recipe_name=request.POST['recipe_name'],
    recipe_category=request.POST['recipe_category'],
    recipe_desc=request.POST['recipe_desc'],
    recipe_ingredient=request.POST['recipe_ingredient'],
    recipe_instruction=request.POST['recipe_instruction'], author=user)
    
    return redirect("recipe:recipe-details", recipe.id)

def recipeShowOne(request, recipe_id):
    pass

def updateRecipe(request):
    # return redirect('recipe:recipe-details')
    pass

def deleteRecipe(request):
    pass