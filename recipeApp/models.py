from django.db import models
from userApp.models import User as UserApp

# Create your models here.
# make your recipe model and finish views next!!

class Recipe(models.Model):

    recipe_name = models.CharField(max_length=255)
    recipe_category = models.CharField(max_length=255)
    recipe_desc = models.TextField()

    # Used for a list of item needed for the recipe
    # will work for now but need to be able to 
    # control how it is added 
    recipe_ingredient = models.TextField()
    recipe_instruction = models.TextField()

    # one to many relationship with user. auto deleted if user
    # is deleted
    recipe_author = models.ForeignKey(UserApp, related_name="recipes", 
    on_delete= models.CASCADE)

    # Auto time feild to track
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __repr__ (self):
        return f"<Recipe object: {self.recipe_name} {self.author} ({self.id})"