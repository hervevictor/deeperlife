from django.contrib import admin
from .models import JeunesPost
from import_export.admin import ImportExportModelAdmin

@admin.register(JeunesPost)
class Usesdd(ImportExportModelAdmin):
    pass 


