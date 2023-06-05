from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Ingredient(models.Model):
    """Describes an ingredient for meals. This ingredient contains specific
    diet and food preference information and can be attached to multiple meals."""
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ingredients = models.TextField(default='')
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    images = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # after creating a recipe the URL redirect
    def get_absolute_url(self):
        return reverse("recipes-detail", kwargs={"pk": self.pk})


class RecipeImage(models.Model):
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return str(self.recipe)
