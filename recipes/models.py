from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    ingredients = models.TextField()
    instructions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # Add more fields as needed

class Tag(models.Model):
    name = models.CharField(max_length=50)
    # Add more fields as needed
    
