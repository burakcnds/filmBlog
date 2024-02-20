
from django.contrib import admin
from django.urls import path
from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',index,name='index'),
    path('film/<slug:f_slug>/',film,name='film-sayfasi'),
    path('film-detay/<slug:d_slug>/',filmDetay,name='film-detay'),
    path('film-kaydet',filmKaydet,name='film-kaydet'),
    path('film-sil/<int:id>/',filmSil,name='film-sil'),
    

] 
