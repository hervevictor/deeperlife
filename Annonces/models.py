from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.urls import reverse


class Annonces(models.Model):
    titre = models.CharField(max_length=200)
    contenu = RichTextField(blank=True, null=True)
    images = models.ImageField(blank=True, null=True, upload_to='images/annonces')
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    add_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.titre
    
    def get_absolute_url(self):
        return reverse("annonces_list")
    class Meta:
        ordering = ['-add_date'] 
    



class DescriptionP(models.Model):
    titre = models.CharField(max_length=200)
    contenu = RichTextField(blank=True, null=True)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    add_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.titre
    
    def get_absolute_url(self):
        return reverse("description_list")

class MotUtilisateur(models.Model):
    titre = models.CharField(max_length=200)
    contenu = RichTextField(blank=True, null=True)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    add_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.titre
    
    def get_absolute_url(self):
        return reverse("mots_list")
     

class ImageDeP(models.Model):
    images = models.ImageField(blank=True, null=True, upload_to='images/annonces')
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    add_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.titre
    
    def get_absolute_url(self):
        return reverse("images_list")
 

