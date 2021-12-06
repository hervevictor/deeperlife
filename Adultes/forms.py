from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import AdultesPost
from Eglises.models import Districts, Groups
from Supports.models import Sexe, Reponses, Region


choices = Districts.objects.all().values_list('name', 'name')
choice = Groups.objects.all().values_list('name', 'name')
reg_choice = Region.objects.all().values_list('name', 'name')
sexs_choice = Sexe.objects.all().values_list('name', 'name')
reponse = Reponses.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)



class AdulteForm(forms.ModelForm):
    class Meta:
        model = AdultesPost
        fields = ('nom', 'prenom', 'date_de_naissance', 'lieu_de_naissance', 'residence', 'district', 'groupe', 
                  'region', 'dirigeant', 'profession', 'sexe', 'groupe_sanguin', 'rhesus', 'role_dans_leglise', 'status_matrimoniale', 'contact', 'contact_whatsapp', 
                  'annee_de_conversion', 'distance_maison_district', 'baptiser', 'annee_de_bapteme',
                  'nombre_d_enfant', 'description_sur_vous_et_votre_famille', 'adulte_images', 'auteur')



        widgets = {
            'nom' : forms.TextInput(attrs={'class': 'form-control'}),
            'prenom' : forms.TextInput(attrs={'class': 'form-control'}),
            'date_de_naissance' : forms.DateInput(attrs={'class': 'form-control'}),
            'lieu_de_naissance' : forms.TextInput(attrs={'class': 'form-control'}),
            'residence' : forms.TextInput(attrs={'class': 'form-control'}),
            'district' : forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'groupe' : forms.Select(choices=choice, attrs={'class': 'form-control'}),
            'region' : forms.Select(choices=reg_choice, attrs={'class': 'form-control'}),
            'dirigeant' : forms.TextInput(attrs={'class': 'form-control'}),
            'profession' : forms.TextInput(attrs={'class': 'form-control'}),
            'sexe' : forms.Select(choices=sexs_choice, attrs={'class': 'form-control'}),
            
            'groupe_sanguin' : forms.TextInput(attrs={'class': 'form-control'}),
            'rhesus' : forms.TextInput(attrs={'class': 'form-control'}),
            'role_dans_leglise' : forms.Select(attrs={'class': 'form-control'}),
            
            'status_matrimoniale' : forms.TextInput(attrs={'class': 'form-control'}),
            'contact' : forms.TextInput(attrs={'class': 'form-control'}),
            'contact_whatsapp' : forms.TextInput(attrs={'class': 'form-control'}),
            'annee_de_conversion' : forms.TextInput(attrs={'class': 'form-control'}),
            'distance_maison_district' : forms.TextInput(attrs={'class': 'form-control'}),
            'baptiser' : forms.widgets.Select(choices=reponse, attrs={'class': 'form-control'}),
            'annee_de_bapteme' : forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_d_enfant' : forms.TextInput(attrs={'class': 'form-control'}),
            'auteur' : forms.Select(attrs={'class': 'form-control'}),

        }


        
