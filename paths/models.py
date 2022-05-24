from django.db import models
import os


class Paths(models.Model):
    foldername = models.CharField(max_length=200)
    parent = models.ForeignKey(
        "self", related_name="paths", on_delete=models.CASCADE)

    def __str__(self) -> str:
        if self.foldername != "/":
            return os.path.join(str(self.parent), self.foldername)
        return "/"

    class Meta:
        unique_together = ("foldername", "parent",)
