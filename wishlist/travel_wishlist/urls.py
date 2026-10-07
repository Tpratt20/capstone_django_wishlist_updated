from django.urls import path
from . import views

#a list of url patterns. Django searches this list until it finds a url section that matches the first argument. 
# second argument specifies which view to call
#  third argument is a name for the url that can be referenced later
urlpatterns = [
    path('', views.place_list, name='place_list'),
    path('visited', views.places_visited,
     name='places_visited'),
    path('place/<int:place_pk>/was_visited', views.place_was_visited, name='place_was_visited'),
    path('about', views.about, name='about'),
    path('place/<int:place_pk>', views.place_details, name='place_details'),
    path('place/<int:place_pk>/delete', views.delete_place, name='delete_place')
]