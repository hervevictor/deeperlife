from django import forms
from django.forms import fields, widgets
from .models import Districts, Groups, Concerne, JeunesDifficultes, Projects
from Supports.models import Region


choices = Region.objects.all().values_list('name', 'name')
choice = Groups.objects.all().values_list('name', 'name')
con_choice = Concerne.objects.all().values_list('name', 'name')
dist_choice = Districts.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)


class DifficultesForm(forms.ModelForm):
    class Meta:
        model = JeunesDifficultes
        fields = ('nom_du_concerne', 'district_du_concerne', 'difficultes', 'groupe_du_concerne', 'region_du_concerne', 'etes_vous', 'auteur')
        
        widgets = {
            'nom_du_concerne' : forms.TextInput(attrs={'class':'form-control'}),
            'district_du_concerne' : forms.Select(choices=dist_choice, attrs={'class':'form-control'}),
            'groupe_du_concerne' : forms.Select(choices=choice,attrs={'class':'form-control'}),
            'region_du_concerne' : forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            'etes_vous' : forms.Select(choices=con_choice, attrs={'class':'form-control'}),
            'auteur' : forms.Select(attrs={'class':'form-control'}),
            
            
        }

class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ('nom_du_concerne', 'district_du_concerne', 'projects', 'groupe_du_concerne', 'region_du_concerne', 'etes_vous', 'auteur')
        
        widgets = {
            'nom_du_concerne' : forms.TextInput(attrs={'class':'form-control'}),
            'district_du_concerne' : forms.Select(choices=dist_choice, attrs={'class':'form-control'}),
            'groupe_du_concerne' : forms.Select(choices=choice,attrs={'class':'form-control'}),
            'region_du_concerne' : forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            'etes_vous' : forms.Select(choices=con_choice, attrs={'class':'form-control'}),
            'auteur' : forms.Select(attrs={'class':'form-control'}),
            
            
        }




class DistrictsForm(forms.ModelForm):
    class Meta:
        model = Districts
        fields = ('name', 'groupe', 'nom_du_pasteur_du_district', 'nom_du_pasteur_du_superviseur', 
                  'nom_du_pasteur_du_superviseur_ajoin', 'nom_du_pasteur_du_groupe', 'region', 'auteur') 

        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'groupe' : forms.Select(choices= choice,attrs={'class':'form-control'}),
            'nom_du_pasteur_du_district' : forms.TextInput(attrs={'class':'form-control'}),
            'nom_du_pasteur_du_superviseur' : forms.TextInput(attrs={'class':'form-control'}),
            'nom_du_pasteur_du_superviseur_ajoin' : forms.TextInput(attrs={'class':'form-control'}),
            'nom_du_pasteur_du_groupe' : forms.TextInput(attrs={'class':'form-control'}),
            'region' : forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            'auteur' : forms.Select(attrs={'class':'form-control'}),
        }



class GroupsForm(forms.ModelForm):
    class Meta:
        model = Groups
        fields = ('name', 'nom_du_pasteur_du_groupe', 'nombre_de_districts', 'region', 'emplacement')
        
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'nom_du_pasteur_du_groupe' : forms.TextInput(attrs={'class':'form-control'}),
            'nombre_de_districts' : forms.TextInput(attrs={'class':'form-control'}),
            'region' : forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            'emplacement' : forms.TextInput(attrs={'class':'form-control'}),
            
        }

