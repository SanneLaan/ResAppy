from django.conf.urls import url
from . import views

app_name = 'recipes'

urlpatterns = [
	# /recipes/
    url(r'^$', views.IndexView.as_view(), name='index'),
	
	# /recipes/<recipe_id>/
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
	
	# /recipes/recipe/add/
	url(r'recipe/add/$', views.RecipeCreate.as_view(), name='recipe-add'),
	
	# /recipes/recipe/2/
	url(r'recipe/(?P<pk>[0-9]+)/$', views.RecipeUpdate.as_view(), name='recipe-update'),
	
	# /recipes/recipe/2/delete/
	url(r'recipe/(?P<pk>[0-9]+)/delete/$', views.RecipeDelete.as_view(), name='recipe-delete'),
	
]

