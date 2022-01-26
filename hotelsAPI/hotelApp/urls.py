from django.urls import path

from . import views

app_name = 'hotelApp'

urlpatterns = [
    path("", views.index, name='index'),
    path("location/<path:search>/", views.locationview, name='location'),
    path("hotels", views.hotelsView, name='hotels'),
    path("hotels/<str:id>", views.hotelsImagesView, name='hotelsImages'),
]