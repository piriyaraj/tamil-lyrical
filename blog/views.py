from django.template.loader import render_to_string
from unittest import result
from django.shortcuts import render

from blog.models import Composer, Lyricist, Movie, Singer, Song

# Create your views here.
def index(request):
    latestMovieObj=Movie.objects.filter().order_by("-id")[:5]
    latestSongObj=Song.objects.filter().order_by("-id")[:10]
    context={
        "latestMovieObj":latestMovieObj,
        'latestSongObj': latestSongObj
    }
    return render(request,'blog/index.html',context)

def blog(request):
    return render(request,'blog/post.html')

def lyrics(request,path):
    songObj=Song.objects.get(slug=path)
    seo = {
        'title': songObj.title+" in tamil" ,
        "description": songObj.title+" telegram "+songObj.title+" invite link Are you searching for active "+songObj.title+" telegram invite link then check out this blog and join the "+songObj.title,
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
    context={
        'movieObj': movieObj,
        'songsObj': songsObj
    }
    return render(request, 'blog/movie.html', context)


def composer(request, path):
    composerObj = Composer.objects.get(slug=path)
    songsObj=Song.objects.filter(composer=composerObj)
    context={
        'composerObj':composerObj,
        "songsObj":songsObj
    }
    return render(request, 'blog/person.html', context)


def lyricist(request, path):
    lyricistObj = Lyricist.objects.get(slug=path)
    songsObj = Song.objects.filter(lyricist=lyricistObj)
    context = {
        'composerObj': lyricistObj,
        "songsObj": songsObj
    }
    return render(request, 'blog/person.html', context)


def singer(request, path):
    singerObj = Singer.objects.get(slug=path)
    songsObj = Song.objects.filter(singer=singerObj)
    context = {
        'composerObj': singerObj,
        "songsObj": songsObj
    }
    return render(request, 'blog/person.html', context)


def year(request, path):
    movieObj = Movie.objects.filter(year=path)
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
