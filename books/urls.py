from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path("product/<int:product_id>/", product, name='product'),
    path("", home),
    path('add/', add_new),
    path('product/<int:product_id>/change/', change_product),
    path('sorted/', sorted),
]