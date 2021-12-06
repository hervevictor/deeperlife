from django.urls import path
from .views import AddDistrict, DistrictList, DistrictDetail, EditDistrict, DeleteDistrict, FilterDistrictGroups, FilterDistrictRegion, \
    AddGroups, GroupsList, GroupsDetail, EditGroups, DeleteGroups, FilterGroupsRegion, \
        AddProjects, ProjectsList, ProjectsDetail, EditProjects, DeleteProjects, FilterProjectsGroups, FilterProjectsRegion, FilterProjectsConcerne, FilterProjectsDistricts, \
            AddDifficultes, DifficultesList, DifficultesDetail, EditDifficultes, DeleteDifficultes, FilterDifficultesGroups, FilterDifficultesRegion, FilterDifficultesConcerne, FilterDifficultesDistricts


urlpatterns = [
    path('add_district', AddDistrict.as_view(), name='add_district'),
    path('district_list', DistrictList.as_view(), name='district_list'),
    path('district/<int:id>', DistrictDetail, name='district_detail'),
    path('district/<int:pk>/edit', EditDistrict.as_view(), name='edit_district'),
    path('district/<int:pk>/delete', DeleteDistrict.as_view(), name='delete_district'),
    path('district_groups/<str:group>', FilterDistrictGroups, name='district_groups'),
    path('district_region/<str:regs>', FilterDistrictRegion, name='district_region'),
    
    
    path('add_group', AddGroups.as_view(), name='add_groups'),
    path('groups_list', GroupsList.as_view(), name='groups_list'),
    path('groups/<int:id>', GroupsDetail, name='groups_detail'),
    path('groups/<int:pk>/edit', EditGroups.as_view(), name='edit_groups'),
    path('groups/<int:pk>/delete', DeleteGroups.as_view(), name='delete_groups'),
    path('groups_region/<str:regs>', FilterGroupsRegion, name='groups_region'),
    
    
    path('add_projects', AddProjects.as_view(), name='add_projects'),
    path('projects_list', ProjectsList.as_view(), name='projects_list'),
    path('projects/<int:id>', ProjectsDetail, name='projects_detail'),
    path('projects/<int:pk>/edit', EditProjects.as_view(), name='edit_projects'),
    path('Projects/<int:pk>/delete', DeleteProjects.as_view(), name='delete_projects'),
    path('projects_groups/<str:group>', FilterProjectsGroups, name='projects_groups'),
    path('projects_region/<str:regs>', FilterProjectsRegion, name='projects_region'),
    path('projects_concerne/<str:vous>', FilterProjectsConcerne, name='projects_concerne'),
    path('projects_district/<str:dist>', FilterProjectsDistricts, name='projects_district'),
    
    
    path('add_difficultes', AddDifficultes.as_view(), name='add_difficultes'),
    path('difficultes_list', DifficultesList.as_view(), name='difficultes_list'),
    path('difficultes/<int:id>', DifficultesDetail, name='difficultes_detail'),
    path('difficultes/<int:pk>/edit', EditDifficultes.as_view(), name='edit_difficultes'),
    path('difficultes/<int:pk>/delete', DeleteDifficultes.as_view(), name='delete_difficultes'),
    path('difficultes_groups/<str:group>', FilterDifficultesGroups, name='difficultes_groups'),
    path('difficultes_region/<str:regs>', FilterDifficultesRegion, name='difficultes_region'),
    path('difficultes_concerne/<str:vous>', FilterDifficultesConcerne, name='difficultes_concerne'),
    path('difficultes_district/<str:dist>', FilterDifficultesDistricts, name='difficultes_district'),
]




 