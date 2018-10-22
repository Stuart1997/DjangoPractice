from django.contrib import admin
from .models import Album, Song

# For each model, add it here so it can viewed in the admin GUI
admin.site.register(Album)
admin.site.register(Song)
