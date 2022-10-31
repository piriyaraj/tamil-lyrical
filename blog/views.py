from django.template.loader import render_to_string
from unittest import result
from django.shortcuts import render

from blog.models import Composer, Lyricist, Movie, Singer, Song

# Create your views here.
def index(request):
    latestMovieObj=Movie.objects.filter().order_by("-id")[:5]
    latestSongObj=Song.objects.filter().order_by("-id")[:10]
    seo = {
        'title': 'Tamil song lyrics | Tamil Lyrical',
        "description": 'Tamil songs lyrics for all movies, lyricist, singers, and composer in Tamil Lyrical',
        "robots": "index, follow",
        "ogimage": '/static/img/logo/logo.png'
    }
    context={
        "latestMovieObj":latestMovieObj,
        'latestSongObj': latestSongObj,
        'seo':seo
    }
    return render(request,'blog/index.html',context)


def lyrics(request,path):
    songObj=Song.objects.get(slug=path)
    singers=""
    for i in(songObj.singer.all()):
        singers+=i.name+", "
    seo = {
        'title': songObj.title+" in tamil" ,
        "description": songObj.title+" From "+songObj.movie.name+" Movie composed by "+songObj.composer.name+", Sung by "+singers+". and Penned by "+songObj.lyricist.name,
        "robots": "index, follow",
        "ogimage": songObj.movie.imageThumb.url
    }
    context = {
        'songObj': songObj,
        'seo': seo
        }
    return render(request, 'blog/lyrics.html',context)


def movie(request, path):
    
    movieObj = Movie.objects.get(slug=path)
    songsObj = Song.objects.filter(movie=movieObj)
    seo = {
        'title': movieObj.name+' movie all songs lyrics | Tamil Lyrical',
        "description": movieObj.name+ 'all songs lyrics in tamil and english',
        "robots": "index, follow",
        "ogimage": movieObj.imageThumb.url
    }
    context={
        'movieObj': movieObj,
        'songsObj': songsObj,
        'seo':seo
    }
    return render(request, 'blog/movie.html', context)


def composer(request, path):
    composerObj = Composer.objects.get(slug=path)
    songsObj=Song.objects.filter(composer=composerObj)
    seo = {
        'title': "Music composer "+composerObj.name+' songs lyrics | Tamil Lyrical',
        "description": "Music composer "+composerObj.name+' all songs lyrics',
        "robots": "index, follow",
        # "ogimage": movieObj.imageThumb.url
    }
    context={
        'composerObj':composerObj,
        "songsObj":songsObj,
        'seo':seo
    }
    return render(request, 'blog/person.html', context)


def lyricist(request, path):
    lyricistObj = Lyricist.objects.get(slug=path)
    songsObj = Song.objects.filter(lyricist=lyricistObj)
    seo = {
        'title': "Lyricist "+lyricistObj.name+' songs lyrics | Tamil Lyrical',
        "description": "Lyricist "+lyricistObj.name+' all songs lyrics',
        "robots": "index, follow",
        # "ogimage": movieObj.imageThumb.url
    }
    context = {
        'composerObj': lyricistObj,
        "songsObj": songsObj,
        'seo': seo
    }
    return render(request, 'blog/person.html', context)


def singer(request, path):
    singerObj = Singer.objects.get(slug=path)
    songsObj = Song.objects.filter(singer=singerObj)
    seo = {
        'title': "Singer "+singerObj.name+' songs lyrics | Tamil Lyrical',
        "description": "Singer "+singerObj.name+' all songs lyrics',
        "robots": "index, follow",
        # "ogimage": movieObj.imageThumb.url
    }
    context = {
        'composerObj': singerObj,
        "songsObj": songsObj,
        'seo':seo
    }
    return render(request, 'blog/person.html', context)


def year(request, path):
    movieObj = Movie.objects.filter(year=path)
    seo = {
        'title': "Best songs in "+path+' lyrics | Tamil Lyrical',
        "description": "Best songs in "+path+' lyrics | Tamil Lyrical',
        "robots": "index, follow",
        # "ogimage": movieObj.imageThumb.url
    }
    context = {
        'movieObj': movieObj,
    }
    return render(request, 'blog/list.html', context)

def test(request):
    result=Song.objects.filter()
    context={
        'result':result
    }
    return render(request, 'blog/test.html',context)



def get_sidebar(request):
    latestMovieObj = Movie.objects.filter().order_by("-id")[:5]
    latestSongObj=Song.objects.filter().order_by("-id")[:5]
    context={
        "latestMovieObj":latestMovieObj,
        'latestSongObj': latestSongObj
    }
    return render(request, "blog/components/sidebar.html", context)

def get_newUpdate(request):
    newupdate = Song.objects.filter().order_by('-id')[:5]

    context={
        'newupdate': newupdate
    }
    return render(request,"blog/components/newupdate.html",context)
