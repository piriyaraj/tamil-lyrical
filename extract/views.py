from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from blog.models import Movie
from . import tools
# Create your views here.
def index(request):
    return render(request,'extract/index.html')


@user_passes_test(lambda u: u.is_superuser)
def getNewLyrics(request):
   
    tools.run()

    return render(request,'extract/index.html')


@user_passes_test(lambda u: u.is_superuser)
def update(request):
    tools.updateUrl()

    return render(request,'extract/index.html')