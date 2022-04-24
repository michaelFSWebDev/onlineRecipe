from django.urls import path
from . import views as recipeViews
app_name ='recipe'


urlpatterns = [
    # Path from userApp to recipeApp
    path('', recipeViews.dashboard, name= "recipe-dashboard" ),

    # Paths to view the Details, update Form, and create form
    path('add/', recipeViews.addForm, name= "recipe-add" ),
    path('recipedetails/int:recipe_id>', recipeViews.recipeDetails, name= "recipe-details" ),
    path('update/<int:recipe_id>', recipeViews.updateForm, name= "recipe-updatepage" ),
    # Paths that will create, update, and Delete the info from database
    path('addrecipe', recipeViews.createRecipe, name= "recipe-create" ),
    path('updateRecipe', recipeViews.updateRecipe, name= "recipe-update" ),
    path('deleterecipe', recipeViews.deleteRecipe, name= "recipe-delete" ),
]