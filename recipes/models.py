from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from .validators import file_size


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ingredients = models.TextField(default='')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Ingredient(models.Model):
        """Describes an ingredient for meals. This ingredient contains specific
        diet and food preference information and can be attached to multiple meals."""
        name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    # after creating a recipe the url redirect
    def get_absolute_url(self):
        return reverse("recipes-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title


class Video(models.Model):
    recipe = models.OneToOneField(Recipe, on_delete=models.CASCADE)
    caption = models.CharField(max_length=100)
    video = models.FileField(upload_to="video/%y", validators=[file_size])

    def __str__(self):
        return self.caption
