from distutils import archive_util
from django.db import models
import os

class ArchiveModel(models.Model):
    """ """
    archive = models.FileField(upload_to ='storage/')

    def __str__(self):
       os.path.basename(self.archive.name) 
