#from django.http import Http404
#from django.http import HttpResponse
#from django.shortcuts import render, get_object_or_404
#from .models import Recipe, Song


#def index(request):
	#all_albums = Recipe.objects.all()
	#context = {'all_albums': all_albums}
	#html = '' 
	#for album in all_albums:
	#	url = '/recipes/' + str(album.id) + '/' 
	#	html += '<a href="' + url + '">' + album.album_title + '</a><br>'
	#return render(request, 'recipes/index.html', {'all_albums': all_albums})
	
	
#def detail(request, album_id):
	#try:
	#	album = Recipe.objects.get(id=album_id)
	#except Recipe.DoesNotExist:
	#	raise Http404("Recipe does not exist")
	#album = get_object_or_404(Recipe, pk=album_id)
	#return render(request, 'recipes/detail.html', {'album': album})
	
#def favorite(request, album_id):
	#album = get_object_or_404(Recipe, pk=album_id)
	#try:
	#	selected_song = album.song_set.get(pk=request.POST['song'])
	#except (KeyError, Song.DoesNotExist):
	#	return render(request, 'recipes/detail.html', {
	#		'album': album,
	#		'error_message': "You did not select a valid song"
	#	})
	#else:
	#	selected_song.is_favorite = True
	#	selected_song.save()
	#	return render(request, 'recipes/detail.html', {'album': album})
	
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
	

class UserFormView(View):
	form_class = UserForm
	template_name = 'recipes/registration_form.html'
	 
	# display blank form
	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})
		
	# process form data		
	def post(self, request):
		form = self.form_class(request.POST)
		
		if form.is_valid():
			
			user = form.save(commit=False)
			
			# cleaned (normalized) data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()
			
			# return User objects if credentials are correct
			user = authenticate(username=username, password=password)
			
			if user is not None:
				
				if user.is_active:
					login(request, user)
					return redirect('recipes:index')
					
		return render(request, self.template_name, {'form': form})
				
				
def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'recipes/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                recipes = Recipe.objects.filter(user=request.user)
                return render(request, 'recipes/index.html', {'albums': albums})
            else:
                return render(request, 'recipes/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'recipes/login.html', {'error_message': 'Invalid login'})
    return render(request, 'recipes/login.html')
				
				
				