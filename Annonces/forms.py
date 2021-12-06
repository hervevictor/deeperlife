from django import forms
from django.db.models import fields
from .models import Annonces, DescriptionP, MotUtilisateur, ImageDeP



class AnnoncesForm(forms.ModelForm):
    class Meta:
        
        model = Annonces
        fields = ('titre', 'contenu', 'images', 'auteur')  
        
        widgets = {
            'titre' : forms.TextInput(attrs={'class':'form-control'}),
            'auteur' : forms.Select(attrs={'class':'form-control'}),
        }


class DescriptionPForm(forms.ModelForm):
    class Meta:
        
        model = DescriptionP
        fields = ('titre', 'contenu', 'auteur')  
        
        widgets = {
            'titre' : forms.TextInput(attrs={'class':'form-control'}),
            'auteur' : forms.Select(attrs={'class':'form-control'}),
        }

class MotUtilisateurForm(forms.ModelForm):
    class Meta:
        
        model = MotUtilisateur
        fields = ('titre', 'contenu', 'auteur')  
        
        widgets = {
            'titre' : forms.TextInput(attrs={'class':'form-control'}),
            'auteur' : forms.Select(attrs={'class':'form-control'}),
        }

       
