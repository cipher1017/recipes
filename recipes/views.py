from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from . import models

from django.core.files.storage import FileSystemStorage


# Create your views here.
# the context is a variable that will create a dictionary of the items, and we pass it to be rendered in the home view

def home(request):
    recipes = models.Recipe.objects.all()
    context = {
        'recipes': recipes,

    }
    return render(request, "recipes/home.html", context)


def upload(request):
    context = {}  # Initialize the context dictionary
    if request.method == 'POST':
        if 'document' in request.FILES:
            uploaded_file = request.FILES['document']
            if uploaded_file:
                fs = FileSystemStorage()
                name = fs.save(uploaded_file.name, uploaded_file)
                context['url'] = fs.url(name)
            else:
                context['message'] = 'Please select a file to upload.'
        else:
            context['message'] = 'No file was found in the request.'
    return render(request, "recipes/upload.html", context)


class RecipeListView(ListView):
    model = models.Recipe
    template_name = 'recipes/home.html'
    # instead of writing every instance of the recipe, we can just override the object
    context_object_name = 'recipes'


class RecipeDetailView(DetailView):
    model = models.Recipe


class RecipeCreateView(CreateView):
    model = models.Recipe
    fields = "__all__"


class RecipeUpdateView(LoginRequiredMixin, CreateView, UserPassesTestMixin, UpdateView):
    model = models.Recipe
    fields = "__all__"

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author


class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Recipe
    success_url = reverse_lazy('recipes-home')

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author


def about(request):
    context = {
        'title': 'about us page'
    }
    return render(request, "recipes/about.html", context)
