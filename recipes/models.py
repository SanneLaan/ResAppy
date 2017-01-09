from django.db import models
from django.core.urlresolvers import reverse


class Recipe(models.Model):
	kitchen = models.CharField(max_length=250, default='e.g. Italian')
	recipe_title = models.CharField(max_length=500, default='e.g. Lasagna')
	recipe_description = models.CharField(max_length=10000, default='What to do?')
	time_in_minutes = models.IntegerField()
	recipe_picture = models.FileField()
	recipe_type = models.CharField(max_length=500, default='e.g. Main Dish')
	ingredient_1 = models.CharField(max_length=500, default='')
	ingredient_2 = models.CharField(max_length=500, default='')
	ingredient_3 = models.CharField(max_length=500, default='')
	
	
	def get_absolute_url(self):
		return reverse('recipes:detail', kwargs={'pk': self.pk})
	
	def __str__(self):
		return self.recipe_title + ' - ' + self.kitchen
	
class Ingredient(models.Model):
	recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
	ingredient_type = models.CharField(max_length=10)
	is_favorite = models.BooleanField(default=False)
	
	def __str__(self):
		return self.recipe_title	
