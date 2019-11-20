from django.shortcuts import render
from testapp.models import Movie
from testapp.forms import MovieForm
# Create your views here.
def base_view(request):
    return render(request, 'testapp/base.html')

def addmovie_view(request):
    form = MovieForm()
    if request.method=='POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return base_view(request)
    return render(request, 'testapp/add_movie.html',{'form1':form})

def movielist_view(request):
    movie_list = Movie.objects.all()
    return render(request, 'testapp/list_movie.html',{'movie_list1' : movie_list})
