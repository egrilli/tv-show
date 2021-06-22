from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('shows',views.show),
    path('shows/new',views.new),
    path('shows/create',views.create),
    path('shows/<id>',views.read),
    path('shows/<id>/edit',views.edit),
    path('shows/<id>/destroy',views.delete),
]