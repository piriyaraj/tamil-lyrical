from django.shortcuts import render

from blog.models import Movie
from . import tools
# Create your views here.
def index(request):
    return render(request,'extract/index.html')

def getNewLyrics(request):
   
    tools.run()

    return render(request,'extract/index.html')