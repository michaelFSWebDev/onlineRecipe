from django.db import models


# Create your models here.
# make your recipe model and finish views next!!

class Recipe(models.Model):

    recipe_name = models.CharField(max_length=255)
    recipe_desc = models.TextField()

    # Used for a list of item needed for the recipe
    # will work for now but need to be able to 
    # control how it is added 
    recipe_ingredient = models.CharField(max_length=255)
    recipe_instruction = models.TextField()

    # one to many relationship with user. auto deleted if user
    # is deleted
    author = models.ForeignKey('userApp.User', related_name="recipes", 
    on_delete= models.CASCADE)

    # Auto time feild to track
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)