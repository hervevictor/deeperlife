from django import forms
from django.forms import fields, widgets
from .models import JeunesPost, OuviresJeunesPost
from Eglises.models import Districts, Groups
from Supports.models import Region, Sexe, Reponses


choices = Districts.objects.all().values_list('name', 'name')
choice = Groups.objects.all().values_list('name', 'name')
reg_choice = Region.objects.all().values_list('name', 'name')
sexs_choice = Sexe.objects.all().values_list('name', 'name')
reponse = Reponses.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)



class JeunePostForm(forms.ModelForm):
    class Meta:
        model = JeunesPost
        fields = ('nom', 'prenom', 'date_de_naissance', 'lieu_de_naissance', 'sexe', 
                  'district','groupe', 'region',  'dirigeant', 'groupe_sanguin', 'rhesus', 'role_dans_leglise', 
                  'numero_de_telephone_du_jeune', 'occupation', 'avec_qui_vit_il', 'nombre_de_freres', 
                  'les_freres_sont_ils_dans_leglise', 'nom_des_freres', 'nombre_de_soeurs',
                  'les_soeurs_sont_elles_dans_leglise', 'nom_des_soeurs', 'nom_des_parentes',
                  'les_parents_sont_ils_dans_leglise', 'numero_de_telephone_des_parents_ou_tuteurs', 
                  'classe_ou_niveau_d_etude', 'Faculte_ou_domaine_d_emploie', 'lieu_de_residence_du_jeune',
                  'distance_maison_district', 'distance_maison_ecole', 'description', 'jeune_images', 'auteur')
        
        widgets = {
            'nom' : forms.TextInput(attrs={'class': 'form-control'}),
            'prenom' : forms.TextInput(attrs={'class': 'form-control'}),
            'date_de_naissance' : forms.DateInput(attrs={'class': 'form-control'}),
            'lieu_de_naissance' : forms.TextInput(attrs={'class': 'form-control'}),
            'sexe' : forms.Select(choices=sexs_choice, attrs={'class': 'form-control'}),
            'district' : forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'groupe' : forms.Select(choices=choice, attrs={'class': 'form-control'}),
            'region' : forms.Select(choices=reg_choice, attrs={'class': 'form-control'}),
            'dirigeant' : forms.TextInput(attrs={'class': 'form-control'}),
            'groupe_sanguin' : forms.TextInput(attrs={'class': 'form-control'}),
            'rhesus' : forms.TextInput(attrs={'class': 'form-control'}),
            'role_dans_leglise' : forms.Select(attrs={'class': 'form-control'}),
            'numero_de_telephone_du_jeune' : forms.NumberInput(attrs={'class': 'form-control'}),
            'occupation' : forms.Select(attrs={'class': 'form-control'}),
            'avec_qui_vit_il' : forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_de_freres' : forms.TextInput(attrs={'class': 'form-control'}),
            'les_freres_sont_ils_dans_leglise' : forms.Select(choices=reponse, attrs={'class': 'form-control'}),
            'nom_des_freres' : forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_de_soeurs' : forms.TextInput(attrs={'class': 'form-control'}),
            'les_soeurs_sont_elles_dans_leglise' : forms.Select(choices=reponse, attrs={'class': 'form-control'}),
            'nom_des_soeurs' : forms.TextInput(attrs={'class': 'form-control'}),
            'nom_des_parentes' : forms.TextInput(attrs={'class': 'form-control'}),
            'les_parents_sont_ils_dans_leglise' : forms.Select(choices=reponse, attrs={'class': 'form-control'}),
            'numero_de_telephone_des_parents_ou_tuteurs' : forms.NumberInput(attrs={'class': 'form-control'}),
            'classe_ou_niveau_d_etude' : forms.TextInput(attrs={'class': 'form-control'}),
            'Faculte_ou_domaine_d_emploie' : forms.TextInput(attrs={'class': 'form-control'}),
            'lieu_de_residence_du_jeune' : forms.TextInput(attrs={'class': 'form-control'}),
            'distance_maison_district' : forms.TextInput(attrs={'class': 'form-control'}),
            'distance_maison_ecole' : forms.TextInput(attrs={'class': 'form-control'}),
            'auteur' : forms.Select(attrs={'class': 'form-control'}),
        }




class OuvrierPostForm(forms.ModelForm):
    class Meta:
        model = OuviresJeunesPost
        fields = ('nom', 'prenom', 'date_de_naissance', 'lieu_de_naissance', 'sexe', 'district','groupe', 'region', 'groupe_sanguin', 
                  'rhesus', 'role_dans_leglise', 'numero_de_telephone1', 'numero_de_telephone2', 'occupation', 
                  'avec_qui_vit_il', 'nombre_de_freres', 'les_freres_sont_ils_dans_leglise', 'nom_des_freres', 
                  'nombre_de_soeurs', 'les_soeurs_sont_elles_dans_leglise', 'nom_des_soeurs', 'nom_des_parentes', 
                  'les_parents_sont_ils_dans_leglise', 'numero_de_telephone_des_parents_ou_tuteurs', 
                  'classe_ou_niveau_d_etude', 'Faculte_ou_domaine_d_emploie', 'lieu_de_residence_du_jeune', 'distance_maison_district', 
                  'distance_maison_lieu_de_travail', 'description', 'ouvrier_images', 'auteur')  


        widgets = {
            'nom' : forms.TextInput(attrs={'class': 'form-control'}),
            'prenom' : forms.TextInput(attrs={'class': 'form-control'}),
            'date_de_naissance' : forms.DateInput(attrs={'class': 'form-control'}),
            'lieu_de_naissance' : forms.TextInput(attrs={'class': 'form-control'}),
            'sexe' : forms.Select(choices=sexs_choice, attrs={'class': 'form-control'}),
            'district' : forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'groupe' : forms.Select(choices=choice, attrs={'class': 'form-control'}),
            'region' : forms.Select(choices=reg_choice, attrs={'class': 'form-control'}),
            'groupe_sanguin' : forms.TextInput(attrs={'class': 'form-control'}),
            'rhesus' : forms.TextInput(attrs={'class': 'form-control'}),
            'role_dans_leglise' : forms.Select(attrs={'class': 'form-control'}),
            'numero_de_telephone1' : forms.NumberInput(attrs={'class': 'form-control'}),
            'numero_de_telephone2' : forms.NumberInput(attrs={'class': 'form-control'}),
            'occupation' : forms.Select(attrs={'class': 'form-control'}),
            'avec_qui_vit_il' : forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_de_freres' : forms.TextInput(attrs={'class': 'form-control'}),
            'les_freres_sont_ils_dans_leglise' : forms.Select(choices=reponse, attrs={'class': 'form-control'}),
            'nom_des_freres' : forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_de_soeurs' : forms.TextInput(attrs={'class': 'form-control'}),
            'les_soeurs_sont_elles_dans_leglise' : forms.Select(choices=reponse, attrs={'class': 'form-control'}),
            'nom_des_soeurs' : forms.TextInput(attrs={'class': 'form-control'}),
            'nom_des_parentes' : forms.TextInput(attrs={'class': 'form-control'}),
            'les_parents_sont_ils_dans_leglise' : forms.Select(choices=reponse, attrs={'class': 'form-control'}),
            'numero_de_telephone_des_parents_ou_tuteurs' : forms.NumberInput(attrs={'class': 'form-control'}),
            'classe_ou_niveau_d_etude' : forms.TextInput(attrs={'class': 'form-control'}),
            'Faculte_ou_domaine_d_emploie' : forms.TextInput(attrs={'class': 'form-control'}),
            'lieu_de_residence_du_jeune' : forms.TextInput(attrs={'class': 'form-control'}),
            'distance_maison_district' : forms.TextInput(attrs={'class': 'form-control'}),
            'distance_maison_lieu_de_travail' : forms.TextInput(attrs={'class': 'form-control'}),
            'auteur' : forms.Select(attrs={'class': 'form-control'}),
        }














