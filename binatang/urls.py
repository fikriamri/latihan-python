from django.urls import path
from . import views

urlpatterns = [
    path('binatang/', views.list_binatang, name='list_binatang'),
    path('input/', views.input_binatang, name='input_binatang'),
]