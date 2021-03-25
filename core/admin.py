from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib import admin
from .models import Profile, Review

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(OSMGeoAdmin):
    list_display = ('user','location')

admin.site.register(Review)
