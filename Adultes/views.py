from django.shortcuts import render
from .models import AdultesPost
from .forms import AdulteForm
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from Eglises.models import Districts, Groups
from Supports.models import Sexe, Region
from django.core.paginator import Paginator
from JeunesApps.resources import AdultesPostResource
from django.http import HttpResponse




def export_data(request):
    if request.method == 'POST':
        # Get selected option from form
        file_format = request.POST['file-format']
        jeunes_resource = AdultesPostResource()
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

    return render(request, 'Adultes/export.html')



def Adulte_liste_tableaux(request):
    District_list = Districts.objects.all()
    Groupe_list = Groups.objects.all()
    Region_list = Region.objects.all()
    adultes_list_tableau = AdultesPost.objects.all()
    adultes_list_tableau_count = AdultesPost.objects.all().count()
    return render(request, 'Adultes/adultes_list_tableau.html', {'adultes_list_tableau':adultes_list_tableau, 'adultes_list_tableau_count':adultes_list_tableau_count, 'District_list':District_list, 'Groupe_list':Groupe_list, 'Region_list':Region_list}) 


class AddAdulteView(CreateView):
    model = AdultesPost
    form_class = AdulteForm
    template_name = 'Adultes/add_adultes.html'


class AdulteListes(ListView):
    model = AdultesPost
    template_name = 'Adultes/adultes_list.html'
    paginate_by = 20
    
    def get_context_data(self, *args, **kwargs):
        District_list = Districts.objects.all()
        Groupe_list = Groups.objects.all()
        Region_list = Region.objects.all()
        Sexe_list = Sexe.objects.all()
        Adulte_nombre = AdultesPost.objects.all().count()
        context = super(AdulteListes, self).get_context_data(*args, **kwargs)
        context["District_list"] = District_list
        context["Groupe_list"] = Groupe_list
        context["Region_list"] = Region_list
        context["Sexe_list"] = Sexe_list
        context["Adulte_nombre"] = Adulte_nombre
        return context

    
def AdultesDetailPost(request, id):
    Adultes_detail = AdultesPost.objects.filter(pk=id)
    Groupe_list = Groups.objects.all()
    Region_list = Region.objects.all()
    return render(request, 'Adultes/adultes_detail.html', {'Adultes_detail':Adultes_detail, 'Groupe_list':Groupe_list, 'Region_list':Region_list}) 


class EditAdultes(UpdateView):
    model = AdultesPost
    template_name = 'Adultes/edite_adultes.html'
    form_class = AdulteForm

class DeleteAdultes(DeleteView):
    model = AdultesPost
    template_name = 'Adultes/delete_adultes.html'
    fields = '__all__'
    success_url = reverse_lazy('adultes_list')     

def Search_Adultes(request): 
    if request.method == 'POST':
        adulte_search = request.POST['adulte_search']
        adultes_nom = AdultesPost.objects.filter(nom__contains=adulte_search)
        adultes_nom_count = AdultesPost.objects.filter(nom__contains=adulte_search).count()
        District_list = Districts.objects.all()
        Groupe_list = Groups.objects.all()
        return render(request, 'Adultes/search_adultes.html', {'adulte_search':adulte_search, 'adultes_nom':adultes_nom, 'adultes_nom_count':adultes_nom_count, 'District_list':District_list, 'Groupe_list':Groupe_list})
    else:
        return render(request, 'Adultes/search_adultes.html', )

def FilterAdultesDistrict(request, dist):
    District_list = Districts.objects.all()
    Adultes_district = AdultesPost.objects.filter(district=dist) 
    Adultes_district_count = AdultesPost.objects.filter(district=dist).count() 
    return render(request, 'Adultes/adultes_district.html', {'Adultes_district':Adultes_district, 'District_list':District_list, 'dist':dist, 'Adultes_district_count':Adultes_district_count})

def FilterAdultesGroupe(request, group):
    Groupe_list = Groups.objects.all()
    Adultes_groupe = AdultesPost.objects.filter(groupe=group)
    Adultes_groupe_count = AdultesPost.objects.filter(groupe=group).count()  
    return render(request, 'Adultes/adultes_groupe.html', {'Adultes_groupe':Adultes_groupe, 'Groupe_list':Groupe_list, 'group':group, 'Adultes_groupe_count':Adultes_groupe_count})

def FilterAdultesRegion(request, regs):
    Region_list = Region.objects.all()
    Adultes_region = AdultesPost.objects.filter(region=regs)
    Adultes_region_count = AdultesPost.objects.filter(region=regs).count()  
    return render(request, 'Adultes/adultes_region.html', {'Adultes_region':Adultes_region, 'regs':regs, 'Region_list':Region_list, 'Adultes_region_count':Adultes_region_count})

def FilterAdultesSexe(request, sexs):
    Sexe_list = Sexe.objects.all()
    Adultes_sexe = AdultesPost.objects.filter(sexe=sexs)
    Adultes_sexe_count = AdultesPost.objects.filter(sexe=sexs).count()  
    return render(request, 'Adultes/adultes_sexe.html', {'Adultes_sexe':Adultes_sexe, 'Sexe_list':Sexe_list, 'sexs':sexs, 'Adultes_sexe_count':Adultes_sexe_count})


def FilterAdultesDistrictTable(request, dist):
    District_list = Districts.objects.all()
    Groupe_list = Groups.objects.all()
    Region_list = Region.objects.all()    
    Adultes_district_tabe = AdultesPost.objects.filter(district=dist) 
    Adultes_district_count_table = AdultesPost.objects.filter(district=dist).count() 
    return render(request, 'Adultes/adultes_district_table.html', {'Adultes_district_tabe':Adultes_district_tabe, 'dist':dist, 'Adultes_district_count_table':Adultes_district_count_table, 'District_list':District_list, 'Groupe_list':Groupe_list, 'Region_list':Region_list})

def FilterAdultesGroupeTable(request, group):
    District_list = Districts.objects.all()
    Groupe_list = Groups.objects.all()
    Region_list = Region.objects.all()
    Adultes_groupe_table = AdultesPost.objects.filter(groupe=group)
    Adultes_groupe_count_table = AdultesPost.objects.filter(groupe=group).count()  
    return render(request, 'Adultes/adultes_groupe_table.html', {'Adultes_groupe_table':Adultes_groupe_table, 'Groupe_list':Groupe_list, 'group':group, 'Adultes_groupe_count_table':Adultes_groupe_count_table , 'District_list':District_list, 'Region_list':Region_list})
         




