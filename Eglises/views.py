from django.shortcuts import render
from .models import Districts, Groups, JeunesDifficultes, Projects, Concerne
from .forms import DistrictsForm, GroupsForm, DifficultesForm, ProjectsForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from Supports.models import Region
from django.core.paginator import Paginator




class AddProjects(CreateView):
    model = Projects
    form_class = ProjectsForm
    template_name = 'Projects/add_projects.html' 

class ProjectsList(ListView):
    model = Projects
    template_name = 'Projects/projects_list.html' 
    paginate_by = 20
    
    def get_context_data(self, *args, **kwargs):
        District_list = Districts.objects.all()
        Groupe_list = Groups.objects.all()
        Region_list = Region.objects.all()
        Projects_nombre = Projects.objects.all().count()
        context = super(ProjectsList, self).get_context_data(*args, **kwargs)
        context["District_list"] = District_list
        context["Groupe_list"] = Groupe_list
        context["Region_list"] = Region_list
        context["Projects_nombre"] = Projects_nombre
        return context

def ProjectsDetail(request, id):
    Projects_detail = Projects.objects.filter(pk=id)
    Region_list = Region.objects.all()
    Groupe_list = Groups.objects.all()
    return render(request, 'Projects/projects_detail.html', {'Projects_detail':Projects_detail, 'Groupe_list':Groupe_list, 'Region_list':Region_list})  

class EditProjects(UpdateView):
    model = Projects
    form_class = ProjectsForm
    template_name = 'Projects/edite_projects.html' 

class DeleteProjects(DeleteView):
    model = Projects
    form_class = ProjectsForm
    template_name = 'Projects/delete_projects.html' 
    success_url = reverse_lazy('projects_list') 

def FilterProjectsConcerne(request, vous):
    Concerne_list = Concerne.objects.all()
    Projects_Concerne = Projects.objects.filter(etes_vous=vous) 
    Projects_Concerne_count = Projects.objects.filter(etes_vous=vous).count()
    return render(request, 'Projects/projects_concerne.html', {'vous':vous, 'Projects_Concerne':Projects_Concerne, 'Projects_Concerne_count':Projects_Concerne_count, 'Concerne_list':Concerne_list})


def FilterProjectsDistricts(request, dist):
    District_list = Districts.objects.all()
    Projects_districts = Projects.objects.filter(district_du_concerne=dist) 
    Projects_districts_count = Projects.objects.filter(district_du_concerne=dist).count()
    return render(request, 'Projects/projects_districts.html', {'dist':dist, 'District_list':District_list, 'Projects_districts':Projects_districts, 'Projects_districts_count':Projects_districts_count})


def FilterProjectsGroups(request, group):
    Groupe_list = Groups.objects.all()
    Projects_groups = Projects.objects.filter(groupe_du_concerne=group) 
    Projects_groups_count = Projects.objects.filter(groupe_du_concerne=group).count()
    return render(request, 'Projects/projects_groups.html', {'group':group, 'Projects_groups':Projects_groups, 'Projects_groups_count':Projects_groups_count, 'Groupe_list':Groupe_list})

def FilterProjectsRegion(request, regs):
    Region_list = Region.objects.all()
    Projects_region = Projects.objects.filter(region_du_concerne=regs) 
    Projects_region_count = Projects.objects.filter(region_du_concerne=regs).count()
    return render(request, 'Projects/projects_region.html', {'regs':regs, 'Projects_region':Projects_region, 'Projects_region_count':Projects_region_count, 'Region_list':Region_list})





class AddDifficultes(CreateView):
    model = JeunesDifficultes
    form_class = DifficultesForm
    template_name = 'Difficultes/add_dfficultes.html' 

class DifficultesList(ListView):
    model = JeunesDifficultes
    template_name = 'Difficultes/difficultes_list.html' 
    paginate_by = 20
    
    def get_context_data(self, *args, **kwargs):
        District_list = Districts.objects.all()
        Groupe_list = Groups.objects.all()
        Region_list = Region.objects.all()
        Difficultes_nombre = JeunesDifficultes.objects.all().count()
        context = super(DifficultesList, self).get_context_data(*args, **kwargs)
        context["District_list"] = District_list
        context["Groupe_list"] = Groupe_list
        context["Region_list"] = Region_list
        context["Difficultes_nombre"] = Difficultes_nombre
        return context

def DifficultesDetail(request, id):
    Difficultes_detail = JeunesDifficultes.objects.filter(pk=id)
    Groups_list = Groups.objects.all()
    Region_list = Region.objects.all()
    return render(request, 'Difficultes/dfficultes_detail.html', {'Difficultes_detail':Difficultes_detail, 'Groups_list':Groups_list, 'Region_list':Region_list})  

class EditDifficultes(UpdateView):
    model = JeunesDifficultes
    form_class = DifficultesForm
    template_name = 'Difficultes/edite_difficultes.html' 

class DeleteDifficultes(DeleteView):
    model = JeunesDifficultes
    form_class = DifficultesForm
    template_name = 'Difficultes/delete_difficultes.html' 
    success_url = reverse_lazy('difficultes_list') 

def FilterDifficultesConcerne(request, vous):
    Concerne_list = Concerne.objects.all()
    Difficultes_Concerne = JeunesDifficultes.objects.filter(etes_vous=vous)
    difficultes_personne = JeunesDifficultes.objects.filter(etes_vous=vous).count() 
    return render(request, 'Difficultes/difficultes_concerne.html', {'vous':vous, 'Difficultes_Concerne':Difficultes_Concerne,'Concerne_list':Concerne_list, 'difficultes_personne':difficultes_personne})


def FilterDifficultesDistricts(request, dist):
    District_list = Districts.objects.all()
    Difficultes_districts = JeunesDifficultes.objects.filter(district_du_concerne=dist) 
    Difficultes_districts_count = JeunesDifficultes.objects.filter(district_du_concerne=dist).count()
    return render(request, 'Difficultes/difficultes_districts.html', {'dist':dist, 'District_list':District_list, 'Difficultes_districts':Difficultes_districts, 'Difficultes_districts_count':Difficultes_districts_count})


def FilterDifficultesGroups(request, group):
    Groupe_list = Groups.objects.all()
    Difficultes_groups = JeunesDifficultes.objects.filter(groupe_du_concerne=group) 
    Difficultes_groups_count = JeunesDifficultes.objects.filter(groupe_du_concerne=group).count()
    return render(request, 'Difficultes/difficultes_groups.html', {'group':group, 'Difficultes_groups':Difficultes_groups, 'Difficultes_groups_count':Difficultes_groups_count, 'Groupe_list':Groupe_list})

def FilterDifficultesRegion(request, regs):
    Region_list = Region.objects.all()
    Difficultes_region = JeunesDifficultes.objects.filter(region_du_concerne=regs) 
    Difficultes_region_count = JeunesDifficultes.objects.filter(region_du_concerne=regs).count()
    return render(request, 'Difficultes/difficultes_region.html', {'regs':regs, 'Difficultes_region':Difficultes_region, 'Difficultes_region_count':Difficultes_region_count, 'Region_list':Region_list})











class AddDistrict(CreateView):
    model = Districts
    form_class = DistrictsForm
    template_name = 'Districts/add_district.html' 

class DistrictList(ListView):
    model = Districts
    template_name = 'Districts/districts_list.html' 
    paginate_by = 20
    
    def get_context_data(self, *args, **kwargs):
        District_list = Districts.objects.all()
        Groupe_list = Groups.objects.all()
        Region_list = Region.objects.all()
        District_nombre = Districts.objects.all().count()
        context = super(DistrictList, self).get_context_data(*args, **kwargs)
        context["District_list"] = District_list
        context["Groupe_list"] = Groupe_list
        context["Region_list"] = Region_list
        context["District_nombre"] = District_nombre
        return context

def DistrictDetail(request, id):
    District_detail = Districts.objects.filter(pk=id)
    Groupe_list = Groups.objects.all()
    Region_list = Region.objects.all()
    return render(request, 'Districts/district_detail.html', {'District_detail':District_detail, 'Groupe_list':Groupe_list, 'Region_list':Region_list})  

class EditDistrict(UpdateView):
    model = Districts
    form_class = DistrictsForm
    template_name = 'Districts/edite_district.html' 

class DeleteDistrict(DeleteView):
    model = Districts
    form_class = DistrictsForm
    template_name = 'Districts/delete_district.html' 
    success_url = reverse_lazy('district_list') 


def FilterDistrictGroups(request, group):
    Groupe_list = Groups.objects.all()
    District_groups = Districts.objects.filter(groupe=group) 
    District_groups_count = Districts.objects.filter(groupe=group).count()
    return render(request, 'Districts/district_groups.html', {'group':group, 'District_groups':District_groups, 'District_groups_count':District_groups_count, 'Groupe_list':Groupe_list})

def FilterDistrictRegion(request, regs):
    Region_list = Region.objects.all()
    District_region = Districts.objects.filter(region=regs) 
    District_region_count = Districts.objects.filter(region=regs).count()
    return render(request, 'Districts/district_region.html', {'regs':regs, 'District_region':District_region, 'District_region_count':District_region_count, 'Region_list':Region_list})




class AddGroups(CreateView):
    model = Groups
    form_class = GroupsForm
    template_name = 'Groups/add_groups.html' 

class GroupsList(ListView):
    model = Groups
    template_name = 'Groups/groups_list.html'
    paginate_by = 20
    
    def get_context_data(self, *args, **kwargs):
        District_list = Districts.objects.all()
        Groupe_list = Groups.objects.all()
        Region_list = Region.objects.all()
        Groupes_nombre = Groups.objects.all().count()
        context = super(GroupsList, self).get_context_data(*args, **kwargs)
        context["District_list"] = District_list
        context["Groupe_list"] = Groupe_list
        context["Region_list"] = Region_list
        context["Groupes_nombre"] = Groupes_nombre
        return context 

def GroupsDetail(request, id):
    Groups_detail = Groups.objects.filter(pk=id)
    Region_list = Region.objects.all()
    return render(request, 'Groups/groups_detail.html', {'Groups_detail':Groups_detail, 'Region_list':Region_list})  

class EditGroups(UpdateView):
    model = Groups
    form_class = GroupsForm
    template_name = 'Groups/edite_groups.html' 

class DeleteGroups(DeleteView):
    model = Groups
    form_class = GroupsForm
    template_name = 'Groups/delete_groups.html' 
    success_url = reverse_lazy('groups_list')

def FilterGroupsRegion(request, regs):
    Region_list = Region.objects.all()
    Groups_region = Groups.objects.filter(region=regs) 
    Groups_region_count = Groups.objects.filter(region=regs).count()
    return render(request, 'Groups/groups_region.html', {'regs':regs, 'Groups_region':Groups_region, 'Groups_region_count':Groups_region_count, 'Region_list':Region_list})

