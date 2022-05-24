import os
from django.db import models
from django.dispatch import receiver
from paths.models import Paths


class Files(models.Model):
    description = models.CharField(max_length=200)
    path = models.ForeignKey(Paths, on_delete=models.CASCADE)
    specs = models.FileField(upload_to='specs')

    def __str__(self) -> str:
        base = os.path.basename(str(self.specs))
        path = str(self.path)
        return os.path.join(path, base)


@receiver(models.signals.post_delete, sender=Files)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `Files` object is deleted.
    """
    if instance.specs and os.path.isfile(instance.specs.path):
        os.remove(instance.specs.path)


@receiver(models.signals.pre_save, sender=Files)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `Files` object is updated
    with new file.
    """
    if not instance.pk:
        return False
