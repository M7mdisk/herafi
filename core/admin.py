from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib import admin
from .models import Profile, Worker, Review

# Register your models here.
@admin.register(Worker)
class WorkerAdmin(OSMGeoAdmin):
    list_display = ('__str__','profile','location')
    fields=("profile","phone_number","bio","location","address","city","professions","rating_average")
    readonly_fields = ("rating_average")

admin.site.register(Profile)
admin.site.register(Review)
