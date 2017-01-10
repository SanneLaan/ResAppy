from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .models import Recipe
from .forms import UserForm

class IndexView(generic.ListView):
	template_name = 'recipes/index.html'
	context_object_name = 'all_recipes'
	
	def get_queryset(self):
		return Recipe.objects.all()
	
	
class DetailView(generic.DetailView):
	model = Recipe
	template_name = 'recipes/detail.html'
	

class RecipeCreate(CreateView):
	model = Recipe 
	fields = ['recipe_title', 'recipe_type', 'kitchen', 'time_in_minutes', 'recipe_description', 'ingredient_1', 'ingredient_2', 'ingredient_3', 'recipe_picture']
	
class RecipeUpdate(UpdateView):
	model = Recipe 
	fields = ['recipe_title', 'recipe_type', 'kitchen', 'time_in_minutes', 'recipe_description', 'ingredient_1', 'ingredient_2', 'ingredient_3', 'recipe_picture']
	
class RecipeDelete(DeleteView):
	model = Recipe
	success_url = reverse_lazy('recipes:index')
	




\
				
				
				