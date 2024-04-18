from django.contrib import admin
from .models import Beat


# Register your models here.

@admin.register(Beat)
class BeatAdmin(admin.ModelAdmin):
    fields = ['name', 'author', ('file', 'cover'), 'description', ('bpm', 'key', 'tags', 'genre'), 'price']
