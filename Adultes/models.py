from django.db import models
from django.contrib.auth.models import User
from Supports.models import Ocupation, Roles
from ckeditor.fields import RichTextField
from django.urls import reverse


class AdultesPost(models.Model):
    nom = models.CharField(max_length=150) 
    prenom = models.CharField(max_length=150)
    date_de_naissance = models.DateField(max_length=150, auto_now_add=False)
    lieu_de_naissance = models.CharField(max_length=150)
    residence = models.CharField(max_length=150)
    district = models.CharField(max_length=150) 
    groupe = models.CharField(max_length=150) 
    region = models.CharField(max_length=150) 
    
    dirigeant = models.CharField(max_length=300)
    
    profession = models.CharField(max_length=150) 
    sexe = models.CharField(max_length=150)
    status_matrimoniale = models.CharField(max_length=150)
    
    groupe_sanguin = models.CharField(max_length=25)
    rhesus = models.CharField(max_length=10)
    role_dans_leglise = models.ForeignKey(Roles, on_delete=models.CASCADE)
    
    contact = models.CharField(max_length=150)
    contact_whatsapp = models.CharField(max_length=150, blank=True, null=True)
    annee_de_conversion = models.CharField(max_length=150)
    distance_maison_district = models.CharField(max_length=100, blank=True, null=True)
    baptiser = models.CharField(max_length=150)
    annee_de_bapteme = models.CharField(max_length=150)
    nombre_d_enfant = models.CharField(max_length=150)
    description_sur_vous_et_votre_famille = RichTextField()
    adulte_images = models.ImageField(blank=True, null=True, upload_to='images/adulte')
    add_date = models.DateField(max_length=150, auto_now_add=True)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nom + '  ' + self.prenom
    
    def get_absolute_url(self):
        return reverse('adultes_list')
    
    
    




