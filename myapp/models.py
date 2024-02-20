from django.db import models
from django.utils.text import slugify
from autoslug import AutoSlugField
# Create your models here.


class Kategori(models.Model):
    name = models.CharField(max_length = 50)
    slug = models.CharField(max_length = 50)

    def __str__(self):
        return self.name


class Filmler(models.Model):
    title = models.CharField(max_length = 50)
    description = models.CharField(max_length = 50)
    image = models.ImageField(upload_to='film-resimleri')
    slug = AutoSlugField(populate_from='title',unique= True)  
    is_active = models.BooleanField(default=False)
    bilgi = models.CharField(max_length = 50)

    # İlişki Yöntemleri
    # 1 - Bir film birden fazla kategoride bulunabilir
    kategori = models.ManyToManyField(Kategori)
    # 2- Bir film bir kategorinin altında bulunabilir
    #kategori = models.ForeignKey
    # 3 - Bir film bir kategoriyle eşleşir ama o kategoriye başka hiçbir şey eklenemez
    #kategori = models.OneToOneField


    def __str__(self):
        return self.title