from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),  # Assuming you have an index view
    path('merge/', views.merge_files, name='merge_files'),  # Keeps existing merge functionality
    path('merge_results/', views.display_merge_results, name='merge_results'),  # New URL for displaying merge results
]
