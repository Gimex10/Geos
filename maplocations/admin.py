from django.contrib import admin
from django.contrib.gis import admin

from maplocations.models import Marker

# Register your models here.

@admin.register(Marker)
class MarkerAdmin(admin.OSMGeoAdmin):

    list_display = ("name", "location")