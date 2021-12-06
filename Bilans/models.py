from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.contrib.auth.models import User



class Cellules(models.Model):
    titre = models.CharField(max_length=200)
    district = models.CharField(max_length=100)
    groupe = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    section = models.CharField(max_length=100)
    billan_de_la_cellule = RichTextField()
    date = models.DateField(auto_now_add=False)
    add_date = models.DateField(auto_now_add=True)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titre
    
    def get_absolute_url(self):
        return reverse("cellules_list")
    
    



class EvenementSpecial(models.Model):
    titre = models.CharField(max_length=200)
    type_d_evenement = models.CharField(max_length=100)
    emplacement = models.CharField(max_length=100)
    billan_de_l_evenement = RichTextField()
    date = models.DateField(auto_now_add=False)
    add_date = models.DateField(auto_now_add=True)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titre
    
    def get_absolute_url(self):
        return reverse("evenements_list")





