from django.urls import path
from .views import AnnoncesList, AddAnnonces, EditAnnonces, DeleteAnnonces, \
DescriptionPList, AddDescriptionP, EditDescriptionP, MotUtilisateurList, AddMotUtilisateur, EditMotUtilisateur, \
   ImageDePList, AddImageDeP , EditImageDeP, DeleteDes


urlpatterns = [
    path('add_annonces', AddAnnonces.as_view(), name='add_annonces'),
    path('annonces_list', AnnoncesList.as_view(), name='annonces_list'),
    path('annonces/<int:pk>/edit', EditAnnonces.as_view(), name='edit_annonces'),
    path('annonces/<int:pk>/remove', DeleteAnnonces.as_view(), name='delete_annonces'),
    
    path('description', DescriptionPList.as_view(), name='description_list'),
    path('add_description', AddDescriptionP.as_view(), name='add_description'),
    path('description/<int:pk>/edit', EditDescriptionP.as_view(), name='edit_description'),
    path('description/<int:pk>/remove', DeleteDes.as_view(), name='delete_description'),
    
    path('mots_list', MotUtilisateurList.as_view(), name='mots_list'),
    path('add_mots', AddMotUtilisateur.as_view(), name='add_mots'),
    path('mots/<int:pk>/edit', EditMotUtilisateur.as_view(), name='edit_mots'),
    
    path('images', ImageDePList.as_view(), name='images_list'),
    path('add_images', AddImageDeP.as_view(), name='add_images'),
    path('images/<int:pk>/edit', EditImageDeP.as_view(), name='edit_images'),

]




