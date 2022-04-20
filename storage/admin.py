from django.contrib import admin
from storage.models import ArchiveModel

# Register your models here.

class StorageAdmin(admin.ModelAdmin):
    """ """
    
admin.site.register(ArchiveModel, StorageAdmin)
