from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField




class Concerne(models.Model):
    name = models.CharField(max_length=300) 
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("concerne_list")



class Districts(models.Model):
    name = models.CharField(max_length=100)
    groupe = models.CharField(max_length=200)
    nom_du_pasteur_du_district = models.CharField(max_length=100)
    nom_du_pasteur_du_superviseur = models.CharField(max_length=100)
    nom_du_pasteur_du_superviseur_ajoin = models.CharField(max_length=100)
    nom_du_pasteur_du_groupe = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    add_date = models.DateField(auto_now_add=True) 

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("district_list")



class Groups(models.Model):
    name = models.CharField(max_length=200)
    nom_du_pasteur_du_groupe = models.CharField(max_length=200)
    nombre_de_districts = models.IntegerField()
    region = models.CharField(max_length=100) 
    emplacement = models.CharField(max_length=300)
    add_date = models.DateField(auto_now_add=True) 
    
    def __str__(self):
        return self.name  
    
    def get_absolute_url(self):
        return reverse("groups_list")
    

    



class JeunesDifficultes(models.Model):
    nom_du_concerne = models.CharField(max_length=200)
    district_du_concerne = models.CharField(max_length=200)
    difficultes = RichTextField(blank=True, null=True)
    groupe_du_concerne = models.CharField(max_length=200)
    region_du_concerne = models.CharField(max_length=200)
    etes_vous = models.CharField(max_length=100)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    add_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.nom_du_concerne
    
    def get_absolute_url(self):
        return reverse("difficultes_list")
     
     

class Projects(models.Model):
    nom_du_concerne = models.CharField(max_length=200)
    projects = RichTextField(blank=True, null=True)
    district_du_concerne = models.CharField(max_length=200)
    groupe_du_concerne = models.CharField(max_length=200)
    region_du_concerne = models.CharField(max_length=200)
    etes_vous = models.CharField(max_length=100)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    add_date = models.DateField(auto_now_add=True) 
    
    def __str__(self):
        return self.nom_du_concerne
    
    def get_absolute_url(self):
        return reverse("projects_list")   




