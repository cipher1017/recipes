from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from . import views

'app/model_view type'
'recipes/recipe_detail.html'

urlpatterns = [
    # we import with .as_view because it is a class in the views
    path('', views.RecipeListView.as_view(), name="recipes-home"),
    path('upload/', views.upload, name="recipes-upload"),
    path('recipe/<int:pk>/', views.RecipeDetailView.as_view(), name="recipes-detail"),
    path('recipe/create', views.RecipeCreateView.as_view(), name="recipes-create"),
    path('recipe/<int:pk>/update', views.RecipeUpdateView.as_view(), name="recipes-update"),
    path('recipe/<int:pk>/delete', views.RecipeDeleteView.as_view(), name="recipes-delete"),
    path('about/', views.about, name="recipes-about"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
