from django.contrib import admin
from storage.models import ArchiveModel, FileModel

# Register your models here.

class StorageAdmin(admin.ModelAdmin):
    """ """
    
admin.site.register(ArchiveModel, StorageAdmin)


class FileAdmin(admin.ModelAdmin):
    """ """
    list_display = ['archive', 'filename']
    
admin.site.register(FileModel, FileAdmin)
