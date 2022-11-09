import re
from unicodedata import name
from bs4 import BeautifulSoup
import requests
from blog.models import Composer, Lyricist, Movie, Singer, Song

from extract.models import ExtractData, PostUrls

mainSitemap = "https://www.tamil2lyrics.com/sitemap.xml"


def getMoviedeatils(url):
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    title = soup.find("h1").text
    year = title.split("(")[1].split(")")[0]
    title = title.split("(")[0]
    try:
        imgUrl = soup.find(
            'div', class_='single-widget').find("img").attrs['src']
    except:
        imgUrl = None
    return year, imgUrl
    pass


def getLastSitemapAndPost():
    try:
        data = ExtractData.objects.get(id=1)
        return data.lastSitemap, data.lastPost
    except:
        " ", " "


def setLastSitemap(lastSitemap):
    ExtractData.objects.filter(id=1).update(lastSitemap=lastSitemap)


def setLastPostLink(postLink):
    ExtractData.objects.filter(id=1).update(lastPost=postLink)


def extractPostLink(url):
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    postLinks = re.findall(
        r'<loc><!\[CDATA\[(.+?)]]></loc>', soup.prettify().replace("\n", "").replace(" ", ""))
    return postLinks


def getSubLyricsSitemap():
    lyricsSitemap = []
    subSitemaps = extractPostLink(mainSitemap)
    for i in subSitemaps:
        if (i.find("lyrics-") > 0):
            lyricsSitemap.append(i)
    return lyricsSitemap


def extractLyrics(postLink):
    reqs = requests.get(postLink)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    songTitle = soup.find("h1").text
    try:
        movieName = soup.find_all(
            "div", {"class": "lyrics-title"})[0].find_all("div")[1].find("a").text
        movieUrl = soup.find_all(
            "div", {"class": "lyrics-title"})[0].find_all("div")[1].find("a").attrs['href']
    except:
        movieName = "-"
        movieUrl = "-"
    try:
        Lyricist = soup.find_all(
            "div", {"class": "lyrics-title"})[0].find("h3").find("a").text
    except:
        Lyricist = "-"

    englishLyrics = "<div id='english'>"
    for i in soup.find("div", {"id": "English"}).find_all("p"):

        if (i.text.find("Singer") >= 0):
            singers = i.text.split(": ")[1].split(" and ")[0].split(", ")
            try:
                singers.append(i.text.split(": ")[1].split(" and ")[1])
            except:
                pass
            continue
        if (i.text.find("Music by") >= 0):
            composer = i.text.split(": ")[1]
            continue
        if (i.text.find("Lyrics by") >= 0):
            continue
        temp = i.text.split(":")
        englishLyrics += "<div class='songp'>"
        englishLyrics += "<div class='songkey'>"+temp[0]+" : "+"</div>"
        try:
            englishLyrics += "<div class='songvalue'>"+temp[1]+"</div>"
        except:
            pass
        englishLyrics += "</div>"
    englishLyrics += "</div>"

    tamilLyrics = "<div id='tamil'>"
    for i in soup.find("div", {"id": "Tamil"}).find_all("p"):
        if (i.text.find("பாடகர்கள் :") >= 0):
            continue
        if (i.text.find("ப்பாளர்  :") >= 0):
            continue
        if (i.text.find("ஆசிரியர் :") >= 0):
            continue
        temp = i.text.split(":")
        tamilLyrics += "<div class='songp'>"
        tamilLyrics += "<div class='songkey'>"+temp[0]+" : "+"</div>"
        try:
            tamilLyrics += "<div class='songvalue'>"+temp[1]+"</div>"
        except:
            pass
        tamilLyrics += "</div>"
    tamilLyrics += "</div>"

    return songTitle, movieName, singers, composer, Lyricist, tamilLyrics, englishLyrics, movieUrl


def feedLyrics(data):
    songTitle, movieName, singers, composer, lyricist, tamilLyrics, englishLyrics, movieUrl = data
    isnewmovie = len(Movie.objects.filter(name=movieName)) == 0
    if (isnewmovie and movieUrl!="-"):
        year, imgUrl = getMoviedeatils(movieUrl)
        # print(imgUrl)
        if (imgUrl == None):
            movieObj = Movie(name=movieName, year=int(year)).save()
        else:
            movieObj = Movie(name=movieName, year=int(
                year), imgUrl=imgUrl).save()
        movieObj = Movie.objects.get(name=movieName)
    else:
        try:
            movieObj = Movie.objects.get(name=movieName)
        except:movieObj=None
    # print("obj", movieObj)
    try:
        composerObj = Composer.objects.create(name=composer)
    except:
        composerObj = Composer.objects.get(name=composer)
    try:
        lyricistObj = Lyricist.objects.create(name=lyricist)
    except:
        lyricistObj = Lyricist.objects.get(name=lyricist)
    singerObjList = []
    for singer in singers:
        try:
            singerObj = Singer.objects.create(name=singer)
        except Exception as e:
            singerObj = Singer.objects.get(name=singer)
        singerObjList.append(singerObj)

    try:
        songObj = Song.objects.create(title=songTitle, songe=englishLyrics, songt=tamilLyrics,
                                      movie=movieObj, lyricist=lyricistObj, composer=composerObj)
    except:
        songObj = Song.objects.get(title=songTitle)
    for i in list(singerObjList):
        songObj.singer.add(i)


def test():
    for i in getSubLyricsSitemap()[:1]:
        for j in extractPostLink(i)[:20]:
            # print(j)
            try:
                feedLyrics(extractLyrics(j))
            except:pass


def run():
    j=PostUrls.objects.filter(status=False)
    # j = "https://www.tamil2lyrics.com/lyrics/enna-marandhen-song-lyrics/"
    for i in j:
        songLyrics = extractLyrics(i)[:50]
        try:
            feedLyrics(songLyrics)
        except:pass

    PostUrls.objects.filter(url=j).update(status=True)

def updateUrl():
    for i in getSubLyricsSitemap():
        for j in extractPostLink(i):
            try:
                PostUrls.objects.create(url=j)
            except:pass
    pass
if __name__ == "__main__":
    url = "https://www.tamil2lyrics.com/movies/maari-2/"
    getMoviedeatils()

    # reqs = requests.get(u4)
    # soup = BeautifulSoup(reqs.text, 'html.parser')
    # singers = ""
    # for i in returnsoup.find("div", {"id": "English"}).find_all("p"):
    #     if (i.text.find("Singer") >= 0):
    #         singer = i.text.split(": ")[1].split(" and ")[0].split(", ")
    #         singer.append(i.text.split(": ")[1].split(" and ")[1])
    #         print(singer)
    #     if (i.text.find("Music by") >= 0):
    #         composer = i.text.split(": ")[1]
    #         print(composer)
