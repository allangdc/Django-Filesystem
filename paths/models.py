from django.db import models
import os


class Paths(models.Model):
    path = models.CharField(max_length=200)
    parent = models.ForeignKey("self", on_delete=models.CASCADE)

    def __str__(self) -> str:
        if self.path != "/":
            return os.path.join(str(self.parent), self.path)
        return "/"

    class Meta:
        unique_together = ("path", "parent",)
