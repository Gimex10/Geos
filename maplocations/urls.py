from django.urls import path

from maplocations.views import MapLocationsView

app_name = "maplocations"

urlpatterns = [
    path("map/", MapLocationsView.as_view(), name="maps"),
]