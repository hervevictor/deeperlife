from django.urls import path
from .views import home, Index, Add_jeunes, JeunesPostDetail, Editjeunes, Deletejeunes, JeunesSearch, FilterJeunesDistrict, \
FilterJeunesGroupe, FilterJeunesRegion, FilterJeunesSexe, Jeunes_tableau_list, FilterJeunesDistrictTable, FilterJeunesGroupeTable, \
    Add_Ouvriers, OuvriersListe, OuvriersDetailPost, EditOuvriers, DeleteOuvriers, Search_ouvriers, \
        FilterOuvriersDistrict, FilterOuvriersGroupe, FilterOuvriersRegion, FilterOuvriersSexe, Ouvriers_tableau_list, \
            FilterOuvriersDistrictTable, FilterOuvriersGroupeTable, export_data, import_data


urlpatterns = [
    path('', home, name="home"),
    path('export_import', export_data, name="export_import"),
    path('import_export', import_data, name="import_export"),
    path('jeunes', Index.as_view(), name="index"),
    path('jeunes_list', Jeunes_tableau_list, name="jeunes_list"),
    path('add_jeune', Add_jeunes.as_view(), name="add_jeunes"),
    path('jeunes/<int:id>', JeunesPostDetail, name="jeunes_detail"),
    path('jeune/<int:pk>/edit', Editjeunes.as_view(), name="edit_jeunes"),
    path('jeune/<int:pk>/remove', Deletejeunes.as_view(), name="delete_jeunes"),
    path('jeunes_search', JeunesSearch, name="jeunes_search"),
    path('district/<str:dist>/', FilterJeunesDistrict, name="jeunes_district"),
    path('groupe/<str:group>/', FilterJeunesGroupe, name="jeunes_groupe"),
    path('region/<str:regs>', FilterJeunesRegion, name="jeune_region"),
    path('sexe/<str:sexs>/', FilterJeunesSexe, name="jeunes_sexe"),
    path('district_table/<str:dist>/', FilterJeunesDistrictTable, name="jeunes_distict_table"),
    path('groupe_table/<str:group>/', FilterJeunesGroupeTable, name="jeunes_groupe_table"),
    
    
    path('add_ouvrier', Add_Ouvriers.as_view(), name="add_ouvriers"),
    path('ouvriers', OuvriersListe.as_view(), name="ouvrier_list"),
    path('ouvrier_tableau_list', Ouvriers_tableau_list, name="ouvrier_tableau_list"),
    path('ouvrier/<int:id>', OuvriersDetailPost, name="ouvriers_detail"),
    path('ouvrier/<int:pk>/edit', EditOuvriers.as_view(), name="edit_ouvriers"),
    path('ouvrier/<int:pk>/remove', DeleteOuvriers.as_view(), name="delete_ouvriers"),
    path('ouvriers_search', Search_ouvriers, name="ouvriers_search"),
    path('district_ouv/<str:dist>/', FilterOuvriersDistrict, name="ouvriers_district"),
    path('groupe_ouv/<str:group>/', FilterOuvriersGroupe, name="ouvriers_groupe"),
    path('region_ouv/<str:regs>', FilterOuvriersRegion, name="region"),
    path('sexe_ouv/<str:sexs>/', FilterOuvriersSexe, name="ouvriers_sexe"),
    path('district_table_ouvrier/<str:dist>/', FilterOuvriersDistrictTable, name="ouvriers_distict_table"),
    path('groupe_table_ouvrier/<str:group>/', FilterOuvriersGroupeTable, name="ouvriers_groupe_table"),
]




