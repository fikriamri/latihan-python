from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('mentee/', views.mentee, name='mentee'),
    path('mentor/', views.mentor, name='mentor'),
    path('author/', views.author, name='author'),
    path('blog/input/', views.input_blog, name='input_blog'),
    path('mentee/input/', views.input_mentee, name='input_mentee'),
    path('mentor/input/', views.input_mentor, name='input_mentor'),
]