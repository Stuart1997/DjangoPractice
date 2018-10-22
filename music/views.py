from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Album, Song


def index(request):
    allAlbums = Album.objects.all()

    return render(request, 'music/index.html', {'allAlbums': allAlbums})


def detail(request, albumID):
    album = get_object_or_404(Album, pk=albumID)

    return render(request, 'music/detail.html', {'album': album})


def favourite(request, albumID):
    album = get_object_or_404(Album, pk=albumID)
    try:
        selectedSong = album.song_set.get(pk=request.POST['song'])
    except(KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {
            'album': album,
            'errorMessage': "Didn't select a valid song"
        })
    else:
        selectedSong.isFavourite = True
        selectedSong.save()
        return render(request, 'music/detail.html', {'album': album})


# Template way without shortcuts
''' from django.template import loader
def index(request):
    allAlbums = Album.objects.all()
    template = loader.get_template('music/index.html')
    context = {'allAlbums': allAlbums}
    return HttpResponse(template.render(context, request))
'''

# def detail pre- getobjector404 import
'''
    try:
        album = Album.objects.get(pk=albumID)
    except Album.DoesNotExist:
        raise Http404("This album does not exist!")
'''