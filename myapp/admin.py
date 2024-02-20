from django.contrib import admin
from .models import *

# Register your models here.
class KategoriAdmin(admin.ModelAdmin):
     list_display = ('name','slug')

     prepopulated_fields = {'slug':['name']}
    

class FilmAdmin(admin.ModelAdmin):
     list_display = ('title','slug','is_active')
     list_editable = ('is_active',)
     search_fields = ('title',)
     # readonly_fields = ['slug']
    
admin.site.register(Kategori,KategoriAdmin)
admin.site.register(Filmler,FilmAdmin)