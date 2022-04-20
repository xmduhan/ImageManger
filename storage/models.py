import os
from distutils import archive_util
from django.db import models
from zipfile import ZipFile
from django.conf import settings


class ArchiveModel(models.Model):
    """ """
    archive = models.FileField(upload_to ='storage/')

    def __str__(self):
       return os.path.basename(self.archive.name) 

    class Meta:
        verbose_name = "压缩包"
        verbose_name_plural = "[01].压缩包"

    def save(self, *args, **kwargs):
        super(ArchiveModel, self).save(*args, **kwargs)
        filename = os.path.join(settings.MEDIA_ROOT, self.archive.name)
        with ZipFile(filename, 'r') as zf:
            for fn in zf.namelist():
                file_model = FileModel()
                file_model.filename = fn
                file_model.archive = self
                file_model.save()

class FileModel(models.Model):
    """ """
    filename = models.CharField('文件名', max_length=1000)
    archive = models.ForeignKey(ArchiveModel, on_delete=models.CASCADE, verbose_name='压缩包')

    def __str__(self):
       return self.filename

    class Meta:
        verbose_name = "文件"
        verbose_name_plural = "[02].文件"