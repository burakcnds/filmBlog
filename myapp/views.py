from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
from django import forms
from django.contrib.auth.decorators import login_required




def index(request):

    
    kategori = Kategori.objects.all()
    #movies = data['movies']
    return render(request,'index.html',{'kategoriler':kategori})
# Create your views here.


def film(request,f_slug):
    kategori = get_object_or_404(Kategori,slug=f_slug)
    film = kategori.filmler_set.filter(is_active = True)
    context = {
        'kategori':kategori,
        'filmler':film
    }


    return render(request,'film.html',context)


def filmDetay(request,d_slug):
    film = Filmler.objects.get(slug = d_slug)
    context = {
        'film':film
    }

    return render(request,'film-detay.html',context)

@login_required(login_url='/login/')

def filmKaydet(request):
    if request.method == 'POST':
        form = FilmKaydet(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request,'film-kaydet.html',{'form':form})
        
    form = FilmKaydet()
    return render(request,'film-kaydet.html',{'form':form})


def filmSil(request,id):
    film = get_object_or_404(Filmler,id = id)
    if request.method == 'POST':
        film.delete()
        return redirect('index')
    context = {
        'film':film
    }
    return render(request,'film-sil.html',context)