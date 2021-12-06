from django.shortcuts import render
from .models import Annonces, DescriptionP, MotUtilisateur, ImageDeP
from .forms import AnnoncesForm, DescriptionPForm, MotUtilisateurForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from Eglises.models import Districts, Groups
from Supports.models import Region
from django.core.paginator import Paginator




class DescriptionPList(ListView):
    model = DescriptionP
    template_name = 'Autres/description_list.html'

    
class AddDescriptionP(CreateView):
    model = DescriptionP
    form_class = DescriptionPForm
    template_name = 'Autres/add_description.html'


class EditDescriptionP(UpdateView):
    model = DescriptionP
    form_class = DescriptionPForm
    template_name = 'Autres/edit_description.html'
 
class DeleteDes(DeleteView):
    model = DescriptionP
    form_class = DescriptionPForm
    template_name = 'Autres/del.html'  
    success_url = reverse_lazy('description_list')  
 


""" Mot à l'gare des user """

class MotUtilisateurList(ListView):
    model = MotUtilisateur
    template_name = 'Autres/mots_list.html'

    
class AddMotUtilisateur(CreateView):
    model = MotUtilisateur
    form_class = MotUtilisateurForm
    template_name = 'Autres/add_mots.html'


class EditMotUtilisateur(UpdateView):
    model = MotUtilisateur
    form_class = MotUtilisateurForm
    template_name = 'Autres/edit_mots.html'
 

""" Images """


class ImageDePList(ListView):
    model = ImageDeP
    template_name = 'Autres/images_list.html'

    
class AddImageDeP(CreateView):
    model = ImageDeP
    fields = '__all__'
    template_name = 'Autres/add_images.html'


class EditImageDeP(UpdateView):
    model = ImageDeP
    fields = '__all__'
    template_name = 'Autres/edit_images.html'
 

""" annonces """







class AnnoncesList(ListView):
    model = Annonces
    template_name = 'annonces_list.html'
    paginate_by = 4
    
    
    def get_context_data(self, *args, **kwargs):
        District_list = Districts.objects.all()
        Groupe_list = Groups.objects.all()
        Region_list = Region.objects.all()
        nombre_annonces = Annonces.objects.all().count()
        context = super(AnnoncesList, self).get_context_data(*args, **kwargs)
        context["District_list"] = District_list
        context["Groupe_list"] = Groupe_list
        context["Region_list"] = Region_list
        context["nombre_annonces"] = nombre_annonces
        return context
    
    
class AddAnnonces(CreateView):
    model = Annonces
    form_class = AnnoncesForm
    template_name = 'add_annonces.html'


class EditAnnonces(UpdateView):
    model = Annonces
    form_class = AnnoncesForm
    template_name = 'edit_annonces.html'

class DeleteAnnonces(DeleteView):
    model = Annonces
    form_class = AnnoncesForm
    template_name = 'delete_annonces.html'  
    success_url = reverse_lazy('annonces_list')  






