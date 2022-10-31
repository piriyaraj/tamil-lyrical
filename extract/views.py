from django.shortcuts import render

from blog.models import Movie
from . import tools
# Create your views here.
def index(request):
    return render(request,'extract/index.html')

def getNewLyrics(request):
    data = ('Ora Siricha Song Lyrics', 'Naam 2', ['MM Manasi', 'Srinisha Jayaseelan', 'Chorus'],
            'Stephen Zechariah', 'Stephen Zechariah', 'tamil', 'english', 'https://www.tamil2lyrics.com/movies/naam-2/')
    # tools.feedLyrics(data)
    tools.test()
    # Movie(name='test1', imgUrl="https://www.tamil2lyrics.com/wp-content/uploads/2022/10/Naam-2-768x432.jpg",year=2021).save()
    lastSiteMap=""
    lastLyricsPost=""

    return render(request,'extract/index.html')