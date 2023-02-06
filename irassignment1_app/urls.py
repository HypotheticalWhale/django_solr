from django.urls import path
from . import views

urlpatterns = [
    path('search_form/', views.search_form, name='search'),
    path('search_results/', views.search_results, name='search_results'),
]
