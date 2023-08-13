from django.urls import path 

from . import views

urlpatterns = [
    path('create-file/',views.create_file),
    path('get-files/', views.get_files),
]