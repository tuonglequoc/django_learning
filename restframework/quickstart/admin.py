from django.contrib import admin
from .models import Movie


class MovieAdmin(admin.ModelAdmin):
    # To reoder fields on the edit form
    fields = ['title', 'year', 'desc']
    # Display in admin
    list_display = ('title', 'year')

admin.site.register(Movie, MovieAdmin)