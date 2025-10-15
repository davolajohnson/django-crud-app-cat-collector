from django.urls import path
from . import views # views are similar to controllers

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('cats/', views.cats_index, name="cat-index"),
    path('cats/<int:cat_id>/', views.cat_detail, name="cat-detail"), # New line for cat detail view
]

