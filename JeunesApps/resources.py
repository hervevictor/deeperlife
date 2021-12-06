from import_export import resources
from .models import JeunesPost
from Adultes.models import AdultesPost
from Enfants.models import EnfantsPost
from LumiereCite.models import BillanDeLumiere, Participants, Etablissements


class AdultesPostResource(resources.ModelResource):
    class Meta:
        model = AdultesPost 
        exclude =  ('description') 
        
class JeunesResource(resources.ModelResource):
    class Meta:
        model = JeunesPost 
        exclude =  ('description') 


class EnfantsPostResource(resources.ModelResource):
    class Meta:
        model = EnfantsPost 
        exclude =  ('description')


class BillanDeLumiereResource(resources.ModelResource):
    class Meta:
        model = BillanDeLumiere 
        exclude =  ('rapports_suggestions')


class ParticipantsResource(resources.ModelResource):
    class Meta:
        model = Participants 
        exclude =  ('probleme_particulier', 'projets')


class EtablissementsResource(resources.ModelResource):
    class Meta:
        model = BillanDeLumiere 
        







