from django.urls import path 
from django.conf import settings 
from django.conf.urls.static import static 
from .import views
urlpatterns = [
    path('',views.index,name='index'),
    path('subscribe/',views.subscribe,name='subscribe'),
    path('buygold/',views.buygold,name='buygold'),
    path('invest/',views.invest,name='invest'),
]
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
