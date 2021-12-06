from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import JeunesPost, OuviresJeunesPost
from django.urls import reverse_lazy
from Eglises.models import Districts, Groups
from Supports.models import Sexe, Region
from .forms import JeunePostForm, OuvrierPostForm
from Enfants.models import EnfantsPost
from django.core.paginator import Paginator
from Annonces.models import Annonces, DescriptionP, MotUtilisateur, ImageDeP
from django.db.models import F
from datetime import timedelta, date 
import datetime
from django.core.paginator import Paginator
from .resources import JeunesResource
from django.http import HttpResponse
from django.contrib.admin.models import LogEntry
from tablib import Dataset
from Adultes.models import AdultesPost





def export_data(request):
    if request.method == 'POST':
        # Get selected option from form
        file_format = request.POST['file-format']
        jeunes_resource = JeunesResource()
        dataset = jeunes_resource.export()
        if file_format == 'CSV':
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="exported_data.csv"'
            return response        
        elif file_format == 'JSON':
            response = HttpResponse(dataset.json, content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename="exported_data.json"'
            return response
        elif file_format == 'XLS (Excel)':
            response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="exported_data.xls"'
            return response   

    return render(request, 'export.html')


def import_data(request):
    if request.method == 'POST':
        file_format = request.POST['file-format']
        employee_resource = JeunesResource()
        dataset = Dataset()
        new_employees = request.FILES['importData']

        if file_format == 'CSV':
            imported_data = dataset.load(new_employees.read().decode('utf-8'),format='csv')
            result = employee_resource.import_data(dataset, dry_run=True)                                                                 
        elif file_format == 'JSON':
            imported_data = dataset.load(new_employees.read().decode('utf-8'),format='json')
            # Testing data import
            result = employee_resource.import_data(dataset, dry_run=True) 

        elif file_format == 'xls':
            imported_data = dataset.load(new_employees.read().decode('utf-8'),format='xls')
            # Testing data import
            result = employee_resource.import_data(dataset, dry_run=True) 

        elif file_format == 'xlsx':
            imported_data = dataset.load(new_employees.read().decode('utf-8'),format='xlsx')
            # Testing data import
            result = employee_resource.import_data(dataset, dry_run=True) 

        if not result.has_errors():
            # Import now
            employee_resource.import_data(dataset, dry_run=False)

    return render(request, 'import.html')    








def home(request):
    Region_list = Region.objects.all()
    Groupe_list = Groups.objects.all()
    nombre_jeunes = JeunesPost.objects.all().count()
    nombre_ouvriers = OuviresJeunesPost.objects.all().count()
    nombre_enfants = EnfantsPost.objects.all().count()
    annonces_list = Annonces.objects.all().order_by('-add_date')[:1]
    nombre_adulte = AdultesPost.objects.all().count()
    nombre_t_jeunes = nombre_jeunes + nombre_ouvriers
    total = nombre_adulte + nombre_t_jeunes + nombre_enfants
    mydate = datetime.datetime.now()
    descriptionP_list = DescriptionP.objects.all()
    motutilisateur_list = MotUtilisateur.objects.all()
    imageDeP_list = ImageDeP.objects.all()
    
    return render(request, 'home.html', {'nombre_jeunes':nombre_jeunes, 'nombre_ouvriers':nombre_ouvriers, 'nombre_enfants':nombre_enfants, 
                                         'Region_list':Region_list, 'total':total, 'annonces_list':annonces_list, 'mydate':mydate, 
                                         'Groupe_list':Groupe_list, 'descriptionP_list':descriptionP_list, 'motutilisateur_list':motutilisateur_list,
                                         'imageDeP_list':imageDeP_list, 'nombre_t_jeunes':nombre_t_jeunes, 'nombre_adulte':nombre_adulte}) 


class Add_Ouvriers(CreateView):
    model = OuviresJeunesPost
    form_class = OuvrierPostForm
    template_name = 'Ouvriers/add_ouvriers.html'
    


class OuvriersListe(ListView):
    model = OuviresJeunesPost
    template_name = 'Ouvriers/ouvriers_list.html'
    paginate_by = 20
    
    def get_context_data(self, *args, **kwargs):
        District_list = Districts.objects.all()
        Groupe_list = Groups.objects.all()
        Region_list = Region.objects.all()
        Sexe_list = Sexe.objects.all()
        nombre_d_ouvriers = OuviresJeunesPost.objects.all().count()
        context = super(OuvriersListe, self).get_context_data(*args, **kwargs)
        context["District_list"] = District_list
        context["Groupe_list"] = Groupe_list
        context["Region_list"] = Region_list
        context["Sexe_list"] = Sexe_list
        context['nombre_d_ouvriers'] = nombre_d_ouvriers
        return context
    
    
def Ouvriers_tableau_list(request):
    Ouvriers_list = OuviresJeunesPost.objects.all()
    Ouvriers_list_count = OuviresJeunesPost.objects.all().count()
    Groupe_list = Groups.objects.all()
    Region_list = Region.objects.all()
    District_list = Districts.objects.all()
    return render(request, 'Ouvriers/ouvrier_tableau_list.html', {'Ouvriers_list':Ouvriers_list, 'Ouvriers_list_count':Ouvriers_list_count, 'Groupe_list':Groupe_list, 'Region_list':Region_list, 'District_list':District_list}) 
   
   
    
def OuvriersDetailPost(request, id):
    Ouvriers_detail = OuviresJeunesPost.objects.filter(pk=id)
    Groupe_list = Groups.objects.all()
    Region_list = Region.objects.all()
    return render(request, 'Ouvriers/ouvriers_detail.html', {'Ouvriers_detail':Ouvriers_detail, 'Region_list':Region_list, 'Groupe_list':Groupe_list}) 


class EditOuvriers(UpdateView):
    model = OuviresJeunesPost
    template_name = 'Ouvriers/edite_ouvriers.html'
    form_class = OuvrierPostForm

class DeleteOuvriers(DeleteView):
    model = OuviresJeunesPost
    template_name = 'Ouvriers/delete_ouvriers.html'
    fields = '__all__'
    success_url = reverse_lazy('ouvrier_list')     

def Search_ouvriers(request):
    if request.method == 'POST':
        ouvrier_search = request.POST['ouvrier_search']
        ouvriers_search = OuviresJeunesPost.objects.filter(nom__contains=ouvrier_search)
        ouvriers_search_count = OuviresJeunesPost.objects.filter(nom__contains=ouvrier_search).count()
        District_list = Districts.objects.all()
        return render(request, 'Ouvriers/search_ouvrier.html', {'ouvrier_search':ouvrier_search, 'ouvriers_search':ouvriers_search, 'ouvriers_search_count':ouvriers_search_count, 'District_list':District_list})
    else:
        return render(request, 'Ouvriers/search_ouvrier.html', )

def FilterOuvriersDistrict(request, dist):
    District_list = Districts.objects.all()
    Ouvriers_district = OuviresJeunesPost.objects.filter(district=dist)
    Ouvriers_district_count = OuviresJeunesPost.objects.filter(district=dist).count() 
    return render(request, 'Ouvriers/ouvriers_district.html', {'Ouvriers_district':Ouvriers_district, 'District_list':District_list, 'dist':dist, 'Ouvriers_district_count':Ouvriers_district_count})

def FilterOuvriersGroupe(request, group):
    Region_list = Region.objects.all()
    Groupe_list = Groups.objects.all()
    Ouvriers_groupe = OuviresJeunesPost.objects.filter(groupe=group)
    Ouvriers_groupe_count = OuviresJeunesPost.objects.filter(groupe=group).count() 
    return render(request, 'Ouvriers/ouvriers_groupe.html', {'Ouvriers_groupe':Ouvriers_groupe, 'Groupe_list':Groupe_list, 'group':group, 'Ouvriers_groupe_count':Ouvriers_groupe_count, 'Region_list':Region_list})

def FilterOuvriersRegion(request, regs):
    Groupe_list = Groups.objects.all()
    Region_list = Region.objects.all()
    Ouvriers_region = OuviresJeunesPost.objects.filter(region=regs)
    Ouvriers_region_count = OuviresJeunesPost.objects.filter(region=regs).count() 
    return render(request, 'Ouvriers/ouvriers_region.html', {'Ouvriers_region':Ouvriers_region, 'regs':regs, 'Region_list':Region_list, 'Ouvriers_region_count':Ouvriers_region_count, 'Groupe_list':Groupe_list})

def FilterOuvriersSexe(request, sexs):
    Sexe_list = Sexe.objects.all()
    Ouvriers_sexe = OuviresJeunesPost.objects.filter(sexe=sexs) 
    Ouvriers_sexe_count = OuviresJeunesPost.objects.filter(sexe=sexs).count()
    return render(request, 'Ouvriers/ouvriers_sexe.html', {'Ouvriers_sexe':Ouvriers_sexe, 'Sexe_list':Sexe_list, 'sexs':sexs, 'Ouvriers_sexe_count':Ouvriers_sexe_count})


def FilterOuvriersDistrictTable(request, dist):
    District_list = Districts.objects.all()
    Region_list = Region.objects.all()
    Groupe_list = Groups.objects.all()
    Ouvriers_district_table = OuviresJeunesPost.objects.filter(district=dist)
    Ouvriers_district_count_table = OuviresJeunesPost.objects.filter(district=dist).count() 
    return render(request, 'Ouvriers/ouvriers_district_table.html', {'Ouvriers_district_table':Ouvriers_district_table, 'District_list':District_list, 'dist':dist, 'Ouvriers_district_count_table':Ouvriers_district_count_table, 'Region_list':Region_list, 'Groupe_list':Groupe_list})

def FilterOuvriersGroupeTable(request, group):
    Region_list = Region.objects.all()
    Groupe_list = Groups.objects.all()
    District_list = Districts.objects.all()
    Ouvriers_groupe_table = OuviresJeunesPost.objects.filter(groupe=group)
    Ouvriers_groupe_count_table = OuviresJeunesPost.objects.filter(groupe=group).count() 
    return render(request, 'Ouvriers/ouvriers_groupe_table.html', {'Ouvriers_groupe_table':Ouvriers_groupe_table, 'Groupe_list':Groupe_list, 'group':group, 'Ouvriers_groupe_count_table':Ouvriers_groupe_count_table, 'Region_list':Region_list, 'District_list':District_list, 'Region_list':Region_list,})

 
         




def FilterJeunesDistrict(request, dist):
    District_list = Districts.objects.all()
    Jeunes_district = JeunesPost.objects.filter(district=dist)
    Jeunes_district_count = JeunesPost.objects.filter(district=dist).count() 
    return render(request, 'jeunes_district.html', {'Jeunes_district':Jeunes_district, 'District_list':District_list, 'dist':dist, 'Jeunes_district_count':Jeunes_district_count})

def FilterJeunesGroupe(request, group):
    Groupe_list = Groups.objects.all()
    Jeunes_groupe = JeunesPost.objects.filter(groupe=group)
    Jeunes_groupe_count = JeunesPost.objects.filter(groupe=group).count() 
    return render(request, 'jeunes_groupe.html', {'Jeunes_groupe':Jeunes_groupe, 'Groupe_list':Groupe_list, 'group':group, 'Jeunes_groupe_count':Jeunes_groupe_count})

def FilterJeunesRegion(request, regs):
    Region_list = Region.objects.all()
    Jeunes_region = JeunesPost.objects.filter(region=regs)
    Jeunes_region_count = JeunesPost.objects.filter(region=regs).count()  
    return render(request, 'jeunes_region.html', {'Jeunes_region':Jeunes_region, 'regs':regs, 'Region_list':Region_list, 'Jeunes_region_count':Jeunes_region_count})

def FilterJeunesSexe(request, sexs):
    Sexe_list = Sexe.objects.all()
    Jeunes_sexe = JeunesPost.objects.filter(sexe=sexs) 
    Jeunes_sexe_count = JeunesPost.objects.filter(sexe=sexs).count()
    return render(request, 'jeunes_sexe.html', {'Jeunes_sexe':Jeunes_sexe, 'Sexe_list':Sexe_list, 'sexs':sexs, 'Jeunes_sexe_count':Jeunes_sexe_count})



def FilterJeunesDistrictTable(request, dist):
    District_list = Districts.objects.all()
    Groupe_list = Groups.objects.all()
    Region_list = Region.objects.all()
    Jeunes_district_table = JeunesPost.objects.filter(district=dist)
    Jeunes_district_count_table = JeunesPost.objects.filter(district=dist).count() 
    return render(request, 'jeunes_distric_table.html', {'Jeunes_district_table':Jeunes_district_table, 'District_list':District_list, 'dist':dist, 'Jeunes_district_count_table':Jeunes_district_count_table, 'Groupe_list':Groupe_list, 'Region_list':Region_list})

def FilterJeunesGroupeTable(request, group):
    Groupe_list = Groups.objects.all()
    District_list = Districts.objects.all()
    Region_list = Region.objects.all()
    Jeunes_groupe_table = JeunesPost.objects.filter(groupe=group)
    Jeunes_groupe_count_table = JeunesPost.objects.filter(groupe=group).count() 
    return render(request, 'jeunes_groupe_table.html', {'Jeunes_groupe_table':Jeunes_groupe_table, 'Groupe_list':Groupe_list, 'group':group, 'Jeunes_groupe_count_table':Jeunes_groupe_count_table, 'District_list':District_list, 'Region_list':Region_list})





class Add_jeunes(CreateView):
    model = JeunesPost
    form_class = JeunePostForm
    template_name = 'add_jeunes.html'
    

def Jeunes_tableau_list(request):
    Jeunes_list = JeunesPost.objects.all()
    Jeunes_list_count = JeunesPost.objects.all().count()
    Groupe_list = Groups.objects.all()
    Region_list = Region.objects.all()
    District_list = Districts.objects.all()
    return render(request, 'jeunes_tabeau_list.html', {'Jeunes_list':Jeunes_list, 'Jeunes_list_count':Jeunes_list_count, 'Groupe_list':Groupe_list, 'Region_list':Region_list, 'District_list':District_list}) 


class Index(ListView):
    model = JeunesPost
    template_name = 'index.html'
    paginate_by = 20
    
    
    def get_context_data(self, *args, **kwargs):
        District_list = Districts.objects.all()
        Groupe_list = Groups.objects.all()
        Region_list = Region.objects.all()
        Sexe_list = Sexe.objects.all()
        nombre_jeunes = JeunesPost.objects.all().count()
        
        #Poster = JeunesPost.objects.all()
        #retrait = JeunesPost.objects.filter(date_de_naissance__gte=date)
        #Tout = Poster.add_date '''
        
        context = super(Index, self).get_context_data(*args, **kwargs)
        context["District_list"] = District_list
        context["Groupe_list"] = Groupe_list
        context["Region_list"] = Region_list
        context["Sexe_list"] = Sexe_list
        context['nombre_jeunes'] = nombre_jeunes
        #context['Tout'] = Tout
        return context
    
     
def JeunesPostDetail(request, id):
    Jeunes_detail = JeunesPost.objects.filter(pk=id)
    Groupe_list = Groups.objects.all()
    Region_list = Region.objects.all()
    return render(request, 'jeunes_detail.html', {'Jeunes_detail':Jeunes_detail, 'Groupe_list':Groupe_list, 'Region_list':Region_list}) 


class Editjeunes(UpdateView):
    model = JeunesPost
    template_name = 'edite_jeunes.html'
    form_class = JeunePostForm

class Deletejeunes(DeleteView):
    model = JeunesPost
    template_name = 'delete_jeunes.html'
    fields = '__all__'
    success_url = reverse_lazy('index')
    


def JeunesSearch(request):
    if request.method == 'POST': 
        searched = request.POST['searched']
        Jeunes_nom = JeunesPost.objects.filter(nom__contains=searched)
        Jeunes_nom_count = JeunesPost.objects.filter(nom__contains=searched).count()
        District_list = Districts.objects.all()
        return render(request, 'jeune_search.html', {'Jeunes_nom':Jeunes_nom, 'Jeunes_nom_count':Jeunes_nom_count, 'searched':searched, 'District_list':District_list})
    else:
        return render(request, 'jeune_search.html')




    
