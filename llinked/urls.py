from django.urls import path, re_path

from llinked import views

urlpatterns = [
    path('search/', views.search, name='search'), 
    # the url path for search must be fixed
]