from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('social',views.social,name='social'),
]