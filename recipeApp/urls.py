from django.urls import path
from . import views as recipeViews
app_name ='recipe'


urlpatterns = [
    path('', recipeViews.dashboard, name= "recipe-dashboard" )
]