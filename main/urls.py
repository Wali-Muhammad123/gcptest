from django.urls import path 
from .import views
urlpatterns = [
    path('',views.index,name='index'),
    path('subscribe/',views.subscribe,name='subscribe'),
    path('buygold/',views.buygold,name='buygold'),
    path('invest/',views.invest,name='invest'),
]