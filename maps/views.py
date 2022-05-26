#from multiprocessing import context
import folium
from django.shortcuts import render, redirect
from .models import Coordinates
from .forms import CoordinatesForm

# Create your views here.

def coordinates_form(request):

    if request.method == 'POST':
        form = CoordinatesForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect("maps")

    
    coordinates = Coordinates.objects.all()
    form =  CoordinatesForm()
    context = {'coordinates': coordinates, 'form':form,}
    return render(request, 'maps/maps_form.html', context)



def maps(request):
    coordinates = list(Coordinates.objects.values_list('lat', 'lon'))[-1]
    
    map =  folium.Map(coordinates)
    folium.Marker(coordinates).add_to(map)
    folium.raster_layers.TileLayer('Stamen Terrain').add_to(map)
    folium.raster_layers.TileLayer('Stamen Toner').add_to(map)
    folium.raster_layers.TileLayer('Stamen Watercolor').add_to(map)
    folium.LayerControl().add_to(map)


    map =  map._repr_html_()
    context = {'map': map,}

    return render(request, 'maps/maps.html', context)