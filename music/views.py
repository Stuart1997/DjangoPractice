from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .models import Album
from .forms import UserForm


# Displays all results as a listview on the index page
class IndexPage(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'album_list'

    def get_queryset(self):
        return Album.objects.all()


# Displays all information about a single album on a detail page
class DetailPage(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'


# What fields need to be filled out in the form?
class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'albumTitle', 'genre', 'albumImage']


# Same details as album create but uses a different View as a parameter
class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'albumTitle', 'genre', 'albumImage']


class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')  # Upon deletion, redirect to index


class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'

    # Display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # Submit form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)  # Creates object from form without saving to db

            # Cleaned/normalised data - formatted properly
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)  # Handles hashed password instead of plaintext
            user.save()  # Saves to db

            # Returns User objects if credentials are correct
            user = authenticate(username=username, password=password)  # Checks if they exist in db

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('music:index')

        return render(request, self.template_name, {'form': form})


# def index(request):
#     allAlbums = Album.objects.all()
#
#     return render(request, 'music/index.html', {'allAlbums': allAlbums})
#
#
# def detail(request, albumID):
#     album = get_object_or_404(Album, pk=albumID)
#
#     return render(request, 'music/detail.html', {'album': album})
#
#
# def favourite(request, albumID):
#     album = get_object_or_404(Album, pk=albumID)
#     try:
#         selectedSong = album.song_set.get(pk=request.POST['song'])
#     except(KeyError, Song.DoesNotExist):
#         return render(request, 'music/detail.html', {
#             'album': album,
#             'errorMessage': "Didn't select a valid song"
#         })
#     else:
#         selectedSong.isFavourite = True
#         selectedSong.save()
#         return render(request, 'music/detail.html', {'album': album})


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
