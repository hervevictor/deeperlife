from django.urls import path
from .views import AddAdulteView, AdulteListes, AdultesDetailPost, EditAdultes, DeleteAdultes, Search_Adultes, \
        FilterAdultesDistrict, FilterAdultesGroupe, FilterAdultesRegion, FilterAdultesSexe, Adulte_liste_tableaux, \
            FilterAdultesDistrictTable, FilterAdultesGroupeTable, export_data


urlpatterns = [
    path('add_adulte', AddAdulteView.as_view(), name='add_adulte'),
    path('adultes_tableau/', Adulte_liste_tableaux, name="adultes_tableau_list"),
    path('adultes_list', AdulteListes.as_view(), name='adultes_list'),
    path('adultes/<int:id>', AdultesDetailPost, name="adultes_detail"),
    path('adulte/<int:pk>/edit', EditAdultes.as_view(), name="edit_adultes"),
    path('adulte/<int:pk>/remove', DeleteAdultes.as_view(), name="delete_adultes"),
    path('adultes_search', Search_Adultes, name="adultes_search"),
    path('district/<str:dist>/', FilterAdultesDistrict, name="adultes_district"),
    path('groupe/<str:group>/', FilterAdultesGroupe, name="adultes_groupe"),
    path('region/<str:regs>', FilterAdultesRegion, name="adultes_region"),
    path('sexe/<str:sexs>/', FilterAdultesSexe, name="adultes_sexe"),
    path('adultes_district_table/<str:dist>/', FilterAdultesDistrictTable, name="adultes_district_table"),
    path('adultes_groupe_table/<str:group>/', FilterAdultesGroupeTable, name="adultes_groupe_table"),
    
    path('adulte_export', export_data, name="adulte_export"),
]




