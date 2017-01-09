from django.conf.urls import url
from . import views

app_name = 'recipes'

urlpatterns = [
	# /recipes/
    url(r'^$', views.IndexView.as_view(), name='index'),
	
	# /recipes/register/
	url(r'^register/$', views.UserFormView.as_view(), name='register'),
	
	# /recipes/login_user
	url(r'^login_user/$', views.login_user, name='login_user'),
    
	# /recipes/logout_user
	url(r'^logout_user/$', views.logout_user, name='logout_user'),
	
	# /recipes/<recipe_id>/
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
	
	# /recipes/recipe/add/
	url(r'recipe/add/$', views.RecipeCreate.as_view(), name='recipe-add'),
	
	# /recipes/recipe/2/
	url(r'recipe/(?P<pk>[0-9]+)/$', views.RecipeUpdate.as_view(), name='recipe-update'),
	
	# /recipes/recipe/2/delete/
	url(r'recipe/(?P<pk>[0-9]+)/delete/$', views.RecipeDelete.as_view(), name='recipe-delete'),
	
	# /recipes/712/
	#url(r'^(?P<recipe_id>[0-9]+)/favorite$', views.favorite, name='favorite'),	
]
