from django.db import models
from django.contrib.auth.models import User
from Supports.models import Ocupation, Roles
from ckeditor.fields import RichTextField
from django.urls import reverse




class JeunesPost(models.Model):
    nom = models.CharField(max_length=100) 
    prenom = models.CharField(max_length=100)
    date_de_naissance = models.DateField(auto_now_add=False, blank=False)
    lieu_de_naissance = models.CharField(max_length=100)
    sexe = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    groupe = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    dirigeant = models.CharField(max_length=300)
    groupe_sanguin = models.CharField(max_length=25)
    rhesus = models.CharField(max_length=10)
    description = RichTextField(blank=True, null=True)
    role_dans_leglise = models.ForeignKey(Roles, on_delete=models.CASCADE)
    numero_de_telephone_du_jeune = models.IntegerField(blank=True, null=True)
    occupation = models.ForeignKey(Ocupation, on_delete=models.CASCADE)
    talents_du_jeune =models.CharField(max_length=400, blank=True, null=True)
    avec_qui_vit_il = models.CharField(max_length=100)
    nombre_de_freres = models.IntegerField()
    les_freres_sont_ils_dans_leglise = models.CharField(max_length=100)
    nom_des_freres = models.CharField(max_length=500)
    nombre_de_soeurs = models.IntegerField()
    les_soeurs_sont_elles_dans_leglise = models.CharField(max_length=100)
    nom_des_soeurs = models.CharField(max_length=500) 
    nom_des_parentes = models.CharField(max_length=400) 
    les_parents_sont_ils_dans_leglise = models.CharField(max_length=100) 
    numero_de_telephone_des_parents_ou_tuteurs = models.IntegerField()
    classe_ou_niveau_d_etude = models.CharField(max_length=200, blank=True, null=True)
    Faculte_ou_domaine_d_emploie = models.CharField(max_length=200, blank=True, null=True)
    lieu_de_residence_du_jeune = models.CharField(max_length=300)
    distance_maison_district = models.CharField(max_length=100, blank=True, null=True)
    distance_maison_ecole = models.CharField(max_length=100, blank=True, null=True)
    jeune_images = models.ImageField(blank=True, null=True, upload_to='images/jeunes')
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    add_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.nom + ' ' +  str(self.prenom)
    
    def get_absolute_url(self):
        return reverse('index') 
    







class OuviresJeunesPost(models.Model):
    nom = models.CharField(max_length=100) 
    prenom = models.CharField(max_length=100)
    date_de_naissance = models.DateField(auto_now_add=False, blank=False)
    lieu_de_naissance = models.CharField(max_length=100)
    sexe = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    groupe = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    groupe_sanguin = models.CharField(max_length=25)
    description = RichTextField(blank=True, null=True)
    rhesus = models.CharField(max_length=10)
    role_dans_leglise = models.ForeignKey(Roles, on_delete=models.CASCADE)
    numero_de_telephone1 = models.IntegerField()
    numero_de_telephone2 = models.IntegerField()
    talents_de_l_ouvrier =models.CharField(max_length=400, blank=True, null=True)
    occupation = models.ForeignKey(Ocupation, on_delete=models.CASCADE)
    avec_qui_vit_il = models.CharField(max_length=100)
    nombre_de_freres = models.IntegerField()
    les_freres_sont_ils_dans_leglise = models.CharField(max_length=100)
    nom_des_freres = models.CharField(max_length=500)
    nombre_de_soeurs = models.IntegerField()
    les_soeurs_sont_elles_dans_leglise = models.CharField(max_length=100)
    nom_des_soeurs = models.CharField(max_length=500) 
    nom_des_parentes = models.CharField(max_length=400) 
    les_parents_sont_ils_dans_leglise = models.CharField(max_length=100)
    numero_de_telephone_des_parents_ou_tuteurs = models.IntegerField() 
    classe_ou_niveau_d_etude = models.CharField(max_length=200, blank=True, null=True)
    Faculte_ou_domaine_d_emploie = models.CharField(max_length=200, blank=True, null=True)
    lieu_de_residence_du_jeune= models.CharField(max_length=300)
    distance_maison_district = models.CharField(max_length=100, blank=True, null=True)
    distance_maison_lieu_de_travail = models.CharField(max_length=100, blank=True, null=True)
    ouvrier_images = models.ImageField(blank=True, null=True, upload_to='images/ouvrier')
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    add_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.nom + '  ' + str(self.prenom)
    
    def get_absolute_url(self):
        return reverse("ouvrier_list")





