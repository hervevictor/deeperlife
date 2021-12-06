from django import forms
from django.forms import fields
from .models import Cellules, EvenementSpecial
from Eglises.models import Districts, Groups, Concerne
from Supports.models import Region


choices = Region.objects.all().values_list('name', 'name')
choice = Groups.objects.all().values_list('name', 'name')
con_choice = Concerne.objects.all().values_list('name', 'name')
dist_choice = Districts.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)


class CellulesForm(forms.ModelForm):
    class Meta:
        model = Cellules
        fields = ('titre', 'district', 'groupe', 'region', 'section', 'billan_de_la_cellule', 'date', 'auteur')

        widgets = {
            
            'titre' : forms.TextInput(attrs={'class':'form-control'}),
            'district' : forms.Select(choices=dist_choice, attrs={'class':'form-control'}),
            'groupe' : forms.Select(choices=choice, attrs={'class':'form-control'}),
            'region' : forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            'section' : forms.Select(choices=con_choice, attrs={'class':'form-control'}),
            'date' : forms.DateInput(attrs={'class':'form-control'}),
            'auteur' : forms.Select(attrs={'class':'form-control'}),
            
        }



class EvenementSpecialForm(forms.ModelForm):
    class Meta:
        model = EvenementSpecial
        fields = ('titre', 'type_d_evenement', 'emplacement', 'billan_de_l_evenement', 'date', 'auteur')

        widgets = {
            
            'titre' : forms.TextInput(attrs={'class':'form-control'}),
            'type_d_evenement' : forms.TextInput(attrs={'class':'form-control'}),
            'emplacement' : forms.TextInput(attrs={'class':'form-control'}),
            'date' : forms.DateInput(attrs={'class':'form-control'}),
            'auteur' : forms.Select(attrs={'class':'form-control'}),
            
        }



